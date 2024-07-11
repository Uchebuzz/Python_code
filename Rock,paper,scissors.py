import random
import time


# name = ("whats your name?  ")
# print()

# def game():
#     timess = int(input(" how many games do you wanna play? "))
#     name = ("whats your name?  ")
#     print()

#     for _ in range (timess):
#         a  = ["rock","paper","scisors"]
#         b = random.randint(0,2)
#         c = a[b]
#         C_choice = (f"computer choice was {a[b]}")
#         gamer_choice = input("Pick a choice (rock, paper or scissors)  ")
#         #for draws
#         if gamer_choice == c:
#                 print(f"{C_choice} its a draw, try again ")
#         #For rock
#         elif gamer_choice == "rock" and c == "scissors":
#             print(f"{C_choice}, you win ")
#         elif gamer_choice == "rock" and c == "paper":
#             print(f"{C_choice}, you loose ")
#         elif gamer_choice == "scissors" and c == "rock":
#                 print(f"{C_choice}, you loose ")
#         elif gamer_choice == "paper" and c == "rock":
#             print(f"{C_choice}, you win ")
            
#         #For paper
#         elif gamer_choice == "paper" and c == "scissors":
#             print(f"{C_choice}, you loose ")
#         elif gamer_choice == "scissors" and c == "paper":
#             print(f"{C_choice}, you win ")

    # #for scissors
    # if gamer_choice == "scissors" and c == "rock":
    #      print(f"{C_choice}, you loose ")
    # if gamer_choice == "paper" and c == "rock":
    #      print(f"{C_choice}, you win ")
         #print(C_choice)
                        
    

#game()


def game():
    choices = ["rock", "paper", "scissors"]
    play_again = "yes"

    while play_again == "yes":
          
        computer_choice = random.choice(choices)
        name = input(("whats your name?  "))
        TimeoutError(2)
        user_choice = input("Pick a choice (rock, paper, or scissors): ").lower()
        
        time.sleep(2)
        print(f"Computer's choice was: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a draw, try again!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print(f"{name}, You win!")
        else:
            print(f"{name}, You lose!")

        play_again = input(f"{name}, Do you want to play again? (yes or no): ").lower()

game()

