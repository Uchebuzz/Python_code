#Guessing Game
import random

#Generate a secret number
secret_number = random.randint(1,10)


#Create a simple loop
while True:
            Guess =  int(input('Guess a number between 1 and 10'))
            

            if Guess > secret_number:
                print('Try again, Too high')
                Guess =  int(input('Guess a number'))
                
            elif Guess < secret_number:
                print('Try again, Too low')
                Guess =  int(input('Guess a number'))
                
            else: Guess == secret_number
            print("congratulations, thats the number!")
            print("bye")
                
            break


