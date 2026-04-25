import random
import numpy as np

options = ("r", "p", "s") # possible game options
playing = True

r = 3  # number of actions
weight_vector = np.ones(r) / r  # initial equal probabilities

a = 0.1  # reward parameter
b = 0.1  # penalty parameter

player_score = 0 # player score tracking
computer_score = 0 # computer score tracking 

def get_index(choice):
    return {"r": 0, "p": 1, "s": 2}[choice]

while playing:

    print(f"Weight vector before: {weight_vector}")

    # Player input
    player = None
    while player not in options:
        player = input("Enter Choice (r, p, s): ").lower()
        if player not in options:
            print("Invalid choice. Try again.")

    # Computer choice (weighted optional, currently random)
    computer = random.choice(options)

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    # Game logic
    if player == computer:
        print("It's a Draw!")
        beta = -1

    elif (player == "r" and computer == "s") or \
         (player == "p" and computer == "r") or \
         (player == "s" and computer == "p"):

        print("Player Wins!")
        player_score += 1
        beta = 1

    else:
        print("Computer Wins!")
        computer_score += 1
        beta = 0

    print(f"Score -> Player: {player_score}, Computer: {computer_score}")

    # Update weights
    idx = get_index(computer)

    if beta == 0:  # computer wins → reward that action
        weight_vector[idx] += a * (1 - weight_vector[idx])
        for j in range(r):
            if j != idx:
                weight_vector[j] *= (1 - a)

    elif beta == 1:  # computer loses → penalize that action
        weight_vector[idx] *= (1 - b)
        for j in range(r):
            if j != idx:
                weight_vector[j] = (b / (r - 1)) + (1 - b) * weight_vector[j]

    # Normalize (important!)
    weight_vector = weight_vector / np.sum(weight_vector)

    print(f"Weight vector after: {weight_vector}")

    # Play again
    while True:
        play_again = input("Play again? (y/n): ").strip().lower()
        if play_again == "y":
            break
        elif play_again == "n":
            playing = False
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

print("Thanks for playing!")
