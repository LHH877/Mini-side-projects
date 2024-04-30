import random  # Import the random module to generate random choices.

user_wins = 0  # Initialize a variable to count the number of wins by the user.
computer_wins = 0  # Initialize a variable to count the number of wins by the computer.

options = ["rock", "paper", "scissors"]  # Define the available options for the game.

while True:  # Start an infinite loop for the game.
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()  # Prompt the user to enter their choice.
    if user_input == "q":  # Check if the user wants to quit the game.
        break  # Exit the loop if the user wants to quit.

    if user_input not in options:  # Check if the user's input is not one of the valid options.
        continue  # Skip the rest of the loop and prompt the user for another input.

    random_number = random.randint(0, 2)  # Generate a random number to represent the computer's choice.
    computer_pick = options[random_number]  # Get the computer's choice based on the random number.
    print("Computer picked", computer_pick + ".")  # Print the computer's choice.

    # Determine the outcome of the game based on the user's choice and the computer's choice.
    if user_input == "rock" and computer_pick == "scissors":
        user_wins += 1
        print("You won!")
    elif user_input == "scissors" and computer_pick == "paper":
        user_wins += 1
        print("You won!")
    elif user_input == "paper" and computer_pick == "rock":
        user_wins += 1
        print("You won!")
    elif user_input == computer_pick:
        print("Draw!")  # Handle the case where both the user and the computer make the same choice.
    else:
        computer_wins += 1
        print("You lost!")  # Handle the case where the computer wins.

# After the game loop ends (when the user quits), print the final results.
print("You won", user_wins, "times!")
print("The computer won", computer_wins, "times!")
print("Goodbye!")  # Print a goodbye message.
