name = input("What is your name: ")  # Ask the user for their name and store it in the variable 'name'.
print("Welcome", name, "to this adventure!")  # Print a welcome message including the user's name.

answer = input("You come to a river, do you want to go (left/right)?").lower()  # Prompt the user to choose a direction and convert the input to lowercase.

if answer == "left":  # Check if the user chose to go left.
    answer = input("You come to a river, do you want to (walk/swim)?").lower()  # Prompt the user for another choice.

    if answer == "swim":  # Check if the user chose to swim.
        print("You swam across the river and died. You lose.")  # Print a message indicating the consequence of the user's choice.
    elif answer == "walk":  # Check if the user chose to walk.
        print("You walked around the river and died. You lose.")  # Print a message indicating the consequence of the user's choice.
    else:
        print("Not a valid option. You lose.")  # Print a message if the user's input is not valid.

elif answer == "right":  # Check if the user chose to go right.
    answer = input("You come to a bridge, do you want to (cross/go back)? ").lower()  # Prompt the user for another choice.

    if answer == "back":  # Check if the user chose to go back.
        print("You go back. You lose.")  # Print a message indicating the consequence of the user's choice.
    elif answer == "cross":  # Check if the user chose to cross the bridge.
        answer = input("You crossed the bridge and saw a stranger, do you want to talk (yes/no)? ").lower()  # Prompt the user for another choice.
        
        if answer == "yes":  # Check if the user chose to talk to the stranger.
            print("The stranger gives you gold. You WIN!")  # Print a message indicating the consequence of the user's choice.
        elif answer == "no":  # Check if the user chose not to talk to the stranger.
            print("The stranger left. You lose.")  # Print a message indicating the consequence of the user's choice.
        else:
            print("Not a valid option. You lose.")  # Print a message if the user's input is not valid.
    else:
        print("Not a valid option. You lose.")  # Print a message if the user's input is not valid.

else:
    print("Not a valid option. You lose.")  # Print a message if the user's input is not valid.

print("Thank you for playing", name)  # Print a message thanking the user for playing the game.
