import random

def roll():
    # Define the minimum and maximum values for a die roll
    min_value = 1
    max_value = 6
    # Generate a random number within the specified range (inclusive)
    roll = random.randint(min_value, max_value)
    return roll

# Loop until a valid number of players (2-4) is entered
while True:
    players = input("Please enter number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        # Check if the number of players is within the allowed range
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players")
    else:
        print("Invalid, try again.")

max_score = 50
# Initialize a list to store the scores of each player, all set to 0 initially
player_scores = [0 for _ in range(players)]

# Main game loop: continue until a player reaches or exceeds the maximum score
while max(player_scores) < max_score:
    # Iterate through each player's turn
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx],"\n")
        current_score = 0

        # Loop for the current player's turn, allowing them to roll the die
        while True:
            should_roll = input("Would you like to roll (y)? ")
            # If the player chooses not to roll, end their turn
            if should_roll.lower() != "y":
                break

            # Roll the die and get a random value
            value = roll()
            # If the roll is a 1, end the turn and reset current score to 0
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                # Otherwise, add the roll value to the current score
                current_score += value
                print("You rolled a:", value)

            # Display the current score for the player
            print("Your score is:", current_score)

        # Update the player's total score with the current score
        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

# Determine the winning player and their score
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)
