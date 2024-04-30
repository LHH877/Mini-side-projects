import random  # Import the random module to generate random numbers.

top_of_range = input("Type a number: ")  # Ask the user to input the maximum value for the range of numbers.

if top_of_range.isdigit():  # Check if the input is a digit.
    top_of_range = int(top_of_range)  # Convert the input to an integer.
    
    if top_of_range <= 0:  # Check if the input is less than or equal to 0.
        print("Please type a number larger than 0 next time.")  # Print a message if the input is not valid.
        quit()  # Exit the program.
else:
    print("Please type a number next time.")  # Print a message if the input is not a digit.
    quit()  # Exit the program.

random_number = random.randint(0, top_of_range)  # Generate a random number within the specified range.
guesses = 0  # Initialize a variable to count the number of guesses made by the user.

while True:  # Start an infinite loop.
    guesses += 1  # Increment the guess counter.
    user_guess = input("Make a guess: ")  # Prompt the user to make a guess.
    if user_guess.isdigit():  # Check if the user's input is a digit.
        user_guess = int(user_guess)  # Convert the user's input to an integer.
    else:
        print("Please type a number next time.")  # Print a message if the input is not a digit.
        continue  # Skip the rest of the loop and prompt the user for another input.

    if user_guess == random_number:  # Check if the user's guess matches the random number.
        print("You got it!")  # Print a message indicating that the user guessed correctly.
        break  # Exit the loop.
    elif user_guess > random_number:  # Check if the user's guess is higher than the random number.
        print("You were above the number!")  # Print a message indicating that the user's guess was too high.
    else:
        print("You were below the number!")  # Print a message indicating that the user's guess was too low.

print("You got it in", guesses, "guesses")  # Print the number of guesses it took for the user to guess the correct number.
