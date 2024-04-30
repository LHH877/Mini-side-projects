import random  # Importing the random module to generate random values

MAX_LINES = 3  # Maximum number of lines that can be bet on
MAX_BET = 100  # Maximum bet amount
MIN_BET = 1  # Minimum bet amount

ROWS = 3  # Number of rows in the slot machine
COLS = 3  # Number of columns in the slot machine

# Dictionary to store the count of each symbol
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# Dictionary to store the value of each symbol
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):  # Function to check for winnings
    winnings = 0  # Initialize winnings to 0
    winning_lines = []  # List to store the winning lines
    for line in range(lines):  # Loop through each line
        symbol = columns[0][line]  # Get the symbol in the first column of the line
        for column in columns:  # Loop through each column in the line
            symbol_to_check = column[line]  # Get the symbol in the current column of the line
            if symbol != symbol_to_check:  # If symbols don't match, break the loop
                break
        else:  # If symbols match for the entire line
            winnings += values[symbol] * bet  # Add winnings for the line
            winning_lines.append(line + 1)  # Add the winning line to the list

    return winnings, winning_lines  # Return total winnings and winning lines


def get_slot_machine_spin(rows, cols, symbols):  # Function to simulate a slot machine spin
    all_symbols = []  # List to store all symbols based on their count
    for symbol, symbol_count in symbols.items():  # Loop through each symbol and its count
        for _ in range(symbol_count):  # Repeat symbol count times
            all_symbols.append(symbol)  # Add symbol to the list

    columns = []  # List to store columns of the slot machine
    for _ in range(cols):  # Loop to generate columns
        column = []  # List to store symbols in a column
        current_symbols = all_symbols[:]  # Copy all symbols for current column
        for _ in range(rows):  # Loop to generate symbols in a column
            value = random.choice(current_symbols)  # Choose a random symbol
            current_symbols.remove(value)  # Remove the chosen symbol from the available symbols
            column.append(value)  # Add the chosen symbol to the column

        columns.append(column)  # Add the column to the slot machine

    return columns  # Return the generated slot machine


def print_slot_machine(columns):  # Function to print the slot machine
    for row in range(len(columns[0])):  # Loop through each row
        for i, column in enumerate(columns):  # Loop through each column
            if i != len(columns) - 1:  # If it's not the last column
                print(column[row], end=" | ")  # Print the symbol followed by a separator
            else:  # If it's the last column
                print(column[row], end="")  # Print the symbol without a separator

        print()  # Move to the next line after printing a row


def deposit():  # Function to deposit money
    while True:  # Repeat until valid input is provided
        amount = input("What would you like to deposit? $")  # Ask user for deposit amount
        if amount.isdigit():  # Check if input is a positive integer
            amount = int(amount)  # Convert input to an integer
            if amount > 0:  # Check if amount is greater than 0
                break  # Break the loop if amount is valid
            else:
                print("Amount must be greater than 0.")  # Print error message if amount is not valid
        else:
            print("Please enter a number.")  # Print error message if input is not a number

    return amount  # Return the deposited amount


def get_number_of_lines():  # Function to get the number of lines to bet on
    while True:  # Repeat until valid input is provided
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")  # Ask user for number of lines
        if lines.isdigit():  # Check if input is a positive integer
            lines = int(lines)  # Convert input to an integer
            if 1 <= lines <= MAX_LINES:  # Check if input is within valid range
                break  # Break the loop if input is valid
            else:
                print("Enter a valid number of lines.")  # Print error message if input is not valid
        else:
            print("Please enter a number.")  # Print error message if input is not a number

    return lines  # Return the number of lines


def get_bet():  # Function to get the bet amount
    while True:  # Repeat until valid input is provided
        amount = input("What would you like to bet on each line? $")  # Ask user for bet amount
        if amount.isdigit():  # Check if input is a positive integer
            amount = int(amount)  # Convert input to an integer
            if MIN_BET <= amount <= MAX_BET:  # Check if input is within valid range
                break  # Break the loop if input is valid
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")  # Print error message if input is not valid
        else:
            print("Please enter a number.")  # Print error message if input is not a number

    return amount  # Return the bet amount


def spin(balance):  # Function to spin the slot machine
    lines = get_number_of_lines()  # Get the number of lines to bet on
    while True:  # Repeat until valid input is provided
        bet = get_bet()  # Get the bet amount
        total_bet = bet * lines  # Calculate the total bet amount

        if total_bet > balance:  # Check if total bet exceeds balance
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")  # Print error message
        else:
            break  # Break the loop if bet is valid

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")  # Print bet information

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)  # Spin the slot machine
    print_slot_machine(slots)  # Print the slot machine
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)  # Check for winnings
    print(f"You won ${winnings}.")  # Print winnings
    print(f"You won on lines:", *winning_lines)  # Print winning lines
    return winnings - total_bet  # Return the net winnings


def main():  # Main function
    balance = deposit()  # Deposit money
    while True:  # Main game loop
        print(f"Current balance is ${balance}")  # Print current balance
        answer = input("Press enter to play (q to quit).")  # Ask user for input to play or quit
        if answer == "q":  # Check if user wants to quit
            break  # Break the loop if user wants to quit
        balance += spin(balance)  # Spin the slot machine and update balance

    print(f"You left with ${balance}")  # Print final balance


main()  # Call the main function to start the game
