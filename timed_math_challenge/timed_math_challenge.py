import random  # Import the random module to generate random numbers
import time  # Import the time module to measure time elapsed during the quiz

# Define a list of operators to be used in arithmetic expressions
OPERATORS = ["+", "-", "*"]
# Define the minimum and maximum values for operands
MIN_OPERAND = 3
MAX_OPERAND = 12
# Define the total number of problems in the quiz
TOTAL_PROBLEMS = 10

# Function to generate a random arithmetic problem
def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)  # Generate a random left operand
    right = random.randint(MIN_OPERAND, MAX_OPERAND)  # Generate a random right operand
    operator = random.choice(OPERATORS)  # Select a random operator

    # Create the arithmetic expression as a string
    expr = str(left) + " " + operator + " " + str(right)
    # Calculate the correct answer for the expression
    answer = eval(expr)
    return expr, answer  # Return the expression and its correct answer

wrong = 0  # Variable to track the number of wrong answers
input("Press enter to start!")  # Wait for user input to start the quiz
print("----------------------------")

start_time = time.time()  # Record the start time of the quiz

# Loop to generate and present arithmetic problems to the user
for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()  # Generate a new problem
    while True:  # Loop until the user provides the correct answer
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")  # Prompt user to guess the answer
        if guess == str(answer):  # If the user's guess matches the correct answer
            break  # Exit the loop
        wrong += 1  # Increment the count of wrong answers

end_time = time.time()  # Record the end time of the quiz
total_time = round(end_time - start_time, 2)  # Calculate the total time taken for the quiz

print("----------------------------")
print("Nice work! You finished in", total_time, "seconds!")  # Display the total time taken to complete the quiz
