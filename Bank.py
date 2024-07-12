# The Customer opens an account
# Deposits money
# Withdraws money
# Makes 
import time
class Bank:
#Deposit = int(input ("How much do you want to deposit? "))
    def bank_opening():
    
        print("Welcome to the bank of life ")
        time.sleep(3)
        name = input("what is your name? ")
        Address = input("what is your Address? ")
        Earnings = int(input("How much do you earn? " ))

        Customer = [name, Address, Earnings, Deposit]

        print(f"Welcome {name}, your ${Deposit} is safe with us") 

    #bank_opening()


    def Withraw():
        print("Welcome to the bank of life ")
        time.sleep(3)
        Acc_details = input("what is your Account detail? ")
        Serect_pin = input("what is your secret pin? ")
        withdraw = int(input("How much do you want to withdraw? " ))
        if withdraw > Deposit :
            print("you don't have sufficient balance")
        elif (withdraw == Deposit) or \
            (withdraw < Deposit):
            print(f"{withdraw} has been withdrawn from your account")
        
    def Bank_app ():
        bank_opening

    Bank_app()

        
