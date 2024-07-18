# The Customer opens an account
# Deposits money
# Withdraws money
# Makes 
import time

def Deposit():
    amount = float(input("Enter an amount to be deposited:$ "))

    if amount < 0:
        print("enter a valid amount") 
        return 0
    else:
        print(f"Thank you for your deposit of ${amount}, it is safe with us")

    return amount
    
    #bank_opening()
def Withraw():
    to_be_withdrawn = float(input("How much do you want to withdraw? $ "))

    if to_be_withdrawn < 0:
        print("enter a valid amount") 
        return 0
    if to_be_withdrawn > balance:
        print("insufficient amount")
        return 0
    else:
        print(f"{to_be_withdrawn} has been deducted from your balance")
        return to_be_withdrawn


def show_balance():
    print(f"your balance is ${balance:.2f}")
    return balance

balance = 0
is_running =True

while is_running:
    print("Welcome to Bank of life")
    time.sleep(3)
    print("")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Balance")
    print("4. Exit")

    choice = input(("what would you like to do today? (1 - 4): "))

    if choice == "1":
       balance -= Withraw()
    elif choice == "2":
       balance += Deposit()
    elif choice == "3":
        show_balance()
    elif choice == "4":
         is_running = False
    else : 
         print("Enter a valid choice")
         
print("Have a nice day")