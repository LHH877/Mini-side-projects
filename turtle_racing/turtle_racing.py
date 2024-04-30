import turtle  # Import the turtle module for creating graphics
import time  # Import the time module for time-related functions
import random  # Import the random module for generating random numbers

# Define constants for the width and height of the window and a list of colors
WIDTH, HEIGHT = 700, 600
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

# Define a function to prompt the user for the number of racers (turtles)
def get_number_of_racers():
    racers = 0
    while True:
        # Prompt the user to input the number of racers
        racers = input('Enter the number of racers (2 - 10): ')
        if racers.isdigit():  # Check if the input is a digit
            racers = int(racers)  # Convert the input to an integer
        else:
            print('Input is not numeric... Try Again!')  # Print error message
            continue

        # Check if the number of racers is within the range of 2 to 10
        if 2 <= racers <= 10:
            return racers  # Return the valid number of racers
        else:
            print('Number not in range 2-10. Try Again!')  # Print error message

# Define a function to simulate the race
def race(colors):
    turtles = create_turtles(colors)  # Create turtle objects with specified colors

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)  # Generate a random distance for each racer
            racer.forward(distance)  # Move the racer forward by the generated distance

            x, y = racer.pos()  # Get the position of the racer
            if y >= HEIGHT // 2 - 10:  # Check if the racer has reached the finish line
                return colors[turtles.index(racer)]  # Return the color of the winning racer

# Define a function to create turtle objects with specified colors
def create_turtles(colors):
    turtles = []  # Initialize an empty list to store turtle objects
    spacingx = WIDTH // (len(colors) + 1)  # Calculate the horizontal spacing between turtles
    for i, color in enumerate(colors):
        racer = turtle.Turtle()  # Create a turtle object
        racer.color(color)  # Set the color of the turtle
        racer.shape('turtle')  # Set the shape of the turtle
        racer.left(90)  # Rotate the turtle to face upwards
        racer.penup()  # Lift the pen to avoid drawing lines
        # Set the initial position of the turtle based on its index and the calculated spacing
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()  # Lower the pen to start drawing
        turtles.append(racer)  # Add the turtle object to the list

    return turtles  # Return the list of turtle objects

# Define a function to initialize the turtle screen
def init_turtle():
    screen = turtle.Screen()  # Create a turtle screen object
    screen.setup(WIDTH, HEIGHT)  # Set up the dimensions of the screen
    screen.title('Turtle Racing!')  # Set the title of the window

racers = get_number_of_racers()  # Get the number of racers from the user
init_turtle()  # Initialize the turtle screen

random.shuffle(COLORS)  # Shuffle the list of colors randomly
colors = COLORS[:racers]  # Select a subset of colors based on the number of racers

winner = race(colors)  # Simulate the race with the selected colors and determine the winner
print("The winner is the turtle with color:", winner)  # Print the color of the winning turtle
time.sleep(5)  # Pause the program for 5 seconds
