import time


def game():
    while True:
        G = input("What is your gender?  ")
        if not G.strip():
            print("I didnt ask for your age, mate.")
        else:
            print(f"So you are {G}?")
            time.sleep(3)
            Guess = input("Can you guess my gender? ")
            break



game()