# Programme for a simple lucky spin jackpot game

#Python Libraries or packings imported
import random

#Constants used in programme
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

#rows and columns in our machine display
ROWS = 3
COLS = 3

#Symbols used in our machine
symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}


symbols_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}





#User deposite funds to wallet
def deposite():
    while True:
        amount = input("Enter the amount you wish to add in to your LuckyJackpot wallet: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number: ")

    return amount

#Asking user about number of line they want to bet on
def get_number_of_lines():
    while True:
        lines = input("Enter the number of line you to bet on (1-"+ str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines: ")
        else:
            print("Please enter a number: ")

    return lines


#How much they want to bet in each line
def get_bet():
    while True:
        amount = input("What would you like to bet on each line: ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}.")
        else:
            print("Please enter a number: ")

    return amount    


#Result geration function for our slot machine
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbols, symbols_count in symbols.items():
        for _ in range(symbols_count):
            all_symbols.append(symbols)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

#printing the result of the slot machine
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end='')
        print()


#checking the win
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line+1)
    return winnings, winning_lines


#Betting game function
def spin(balance):
    lines = get_number_of_lines()
    #checking user have enough funds in wallet for the bet
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You doesn't have enough fund in your wallet, your current balance is {balance}.")
        else:
            break

    
    print(f"You are betting {bet} on {lines} lines. Total bet is equal to: {total_bet}.")
    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbols_values)
    print(f"You won : {winnings}.")
    print(f"You won on lines : ", *winning_lines)
    return winnings - total_bet




# Main function of the programme
def main():
    balance = deposite()
    while True:
        print(f"Your current balance is {balance}.")
        answer = input("Press enter to play (q to quit): ")
        if answer == 'q':
            break
        balance += spin(balance)
    
    print(f"You left with {balance}.")

main()