# Function to view existing passwords
def view():
    # Open the password file in read mode
    with open("password.txt","r") as f:
        # Read each line in the file
        for line in f.readlines():
            # Remove any trailing whitespace
            data = line.rstrip()
            # Split the line into username and password
            user, passw = data.split()
            # Print the username and password
            print("User:", user, "Password:", passw)

# Function to add a new password
def add():
    # Prompt the user for the account name and password
    name = input("Account name: ")
    pwd = input("Password: ")

    # Open the password file in append mode
    with open("password.txt","a") as f:
        # Write the account name and password to the file, separated by "|"
        f.write(name + "|" + pwd + "\n")

# Main loop to interact with the user
while True:
    # Prompt the user for the desired action
    mode = input("Would you like to add a new password or view existing ones? (add/view), enter q to quit ").lower()

    # Check the user's input
    if mode == "q":  # If the user wants to quit, break out of the loop
        break
    elif mode == "add":  # If the user wants to add a password, call the add function
        add()
    elif mode == "view":  # If the user wants to view passwords, call the view function
        view()
    else:  # If the input is invalid, prompt the user again
        print("Invalid mode.")
        continue
