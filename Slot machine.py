import random 

#declearing important variables

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

ROWS = 3
COLS = 3


Symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

Symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def slot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, Symbol_count in symbols.items():
        for _ in range (Symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range (cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range (rows):
            value= random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_slot_machines(columns):
    for row in range (len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print (columns[row],end= "|")
            else:
                print(column[row], end= "" )
print()


def check_win (columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol !=symbol_to_check:
                break
    else:
        winnings += values [symbol] * bet
        winning_lines.append(line + 1)
    return winnings, winning_lines


def deposit ():
    while True:
        amount = input("what would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 :
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("please enter a number")
    return amount

#deposit()

def numberline():
    while True:
        lines = input("Enter the number of lines(1 - " + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("please a valid number")
    return lines

#numberline()

def get_bet():
    while True:
        amount = input("what would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("please enter a valid bet")
    return amount

#get_bet()

def spin(balance):
    lines = numberline()
    while True:
        bet = get_bet()
        Total_bet = bet * lines
        if Total_bet > balance:
            print(f"You do not have enough to bet that amount on, your balance is ${balance}")
        else:
            break

    print (f"you are betting ${bet} on {lines} lines. Total bet is equal to ${Total_bet}")
    slots = slot_spin(ROWS, COLS, Symbol_count)
    print_slot_machines(slots)
    winnings, winning_line = check_win(slots,lines,bet,Symbol_values)
    print(f"you won ${winnings}")
    # print(f"you won on lines:", *{winning_line})
    return winnings - Total_bet



def main():
    balance = deposit()
    while True:
        print(f'Current balance is ${balance}')
        answer = input("press enter to paly(q to quit) (w to check balance)  ")
        if answer == "w":
            print(f"Your current balance is ${balance} ")
        elif answer == "q":
            break
        balance += spin(balance)
    print(f"you are left witth ${balance}")




main()

