#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

import random

# Define a function to play Rock, Paper, Scissors
def play_rock_paper_scissors():
    # Create a list of available choices
    options = ["rock", "paper", "scissors"]
    
    # Initialize variables to track wins and losses
    wins = 0
    losses = 0

    # Start a game loop
    while True:
        # Ask the player to choose an option or quit
        player_choice = input("Choose rock, paper, or scissors (or 'quit' to end the game): ").lower()

        # Check if the player wants to quit the game
        if player_choice == 'quit':
            break
        # Check if the player's choice is not valid
        elif player_choice not in options:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Generate a random choice for the computer
        computer_choice = random.choice(options)
        print(f"The computer chose: {computer_choice}")

        # Determine the winner of the round
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!")
            wins += 1
        else:
            print("You lose this round.")
            losses += 1

    # Display the final score to the player
    print(f"Total wins: {wins}")
    print(f"Total losses: {losses}")
    print("Thanks for playing!")

# Check if the script is executed as the main program
if __name__ == "__main__":
    play_rock_paper_scissors()
