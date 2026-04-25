# Reinforcement Learning 

## Rock-Paper-Scissors Game

### Overview
This project is a Rock-Paper-Scissors game that implements reinforcement learning.
The computer adapts its strategy over time by updating a probability weight vector based on game outcomes.

The goal is to demonstrate how basic learning systems can adjust behaviour through reward and penalty updates.

### Key Features
- Classic Rock-Paper-Scissors game logic
- Adaptive AI opponent using a weight-based learning system
- Dynamic probability updates after each round
- Score tracking for player vs computer
- Continuous play option with input validation

### How It Works

The computer maintains a **weight vector** representing the probability of selecting:
- Rock (r)
- Paper (p)
- Scissors (s)

### Learning Mechanism:
- If the computer wins → it reinforces the chosen action (reward)
- If the computer loses → it reduces the probability of that action (penalty)
- If there is a draw → no strong update is applied

The weight vector is normalized after each round so probabilities always sum to 1.

### Logic Summary

- Actions: `r`, `p`, `s`
- Weight vector initialized equally: `[0.33, 0.33, 0.33]`
- Reward parameter: `a = 0.1`
- Penalty parameter: `b = 0.1`

The system updates probabilities dynamically based on outcomes and gradually adjusts strategy.

### Technologies Used
- Python 
- NumPy
- Random library 
