import random
import time


Rock = 0
Paper = 1
Scissors = 2

name = ("whats your name?  ")

def game():
    timess = int(input(f"{name}, how many games do you wanna play? "))
    for i in range (timess):
        a  = ["rock","paper","scisors"]
        b = random.randint(0,2)
        c = a[b]
    C_choice = (f"computer choice was {a[b]}")
    gamer_choice = input("Pick a choice (Rock, paper or scissors)  ")
    if C_choice == gamer_choice:
            print("its a draw, try again ")

game()
      