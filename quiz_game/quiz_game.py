print("Welcome to my computer quiz!")  # Print a welcome message to the user.

playing = input("Do you want to play? ")  # Ask the user if they want to play the quiz and store their response.

if playing.lower() != "yes":  # Check if the user's response is not "yes" (case insensitive).
    quit()  # If the response is not "yes", quit the program.

print("Okay! Let's play!")  # If the response is "yes", print a confirmation message that the game is starting.
score = 0  # Initialize the score variable to keep track of the user's score.

answer = input("What does CPU stand for? ")  # Ask the user the first question and store their answer.
if answer.lower() == "central processing unit":  # Check if the user's answer matches the correct answer (case insensitive).
    print("Correct!")  # If the answer is correct, print a message indicating correctness.
    score += 1  # Increment the score by 1.
else:
    print("Incorrect!")  # If the answer is incorrect, print a message indicating incorrectness.

answer = input("What does GPU stand for? ")  # Ask the user the second question and store their answer.
if answer.lower == "graphics processing unit":  # Check if the user's answer matches the correct answer (case insensitive).
    print("Correct!")  # If the answer is correct, print a message indicating correctness.
    score += 1  # Increment the score by 1.
else:
    print("Incorrect!")  # If the answer is incorrect, print a message indicating incorrectness.

print("You got " + str(score) + " questions correct!")  # Print the user's total score.
print("You got " + str((score/2) *100) + "%.")  # Calculate and print the percentage of correct answers.
