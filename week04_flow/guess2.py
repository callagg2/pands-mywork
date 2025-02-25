# this program prompts you to continually guess a number, telling you if the guess is too high or too low, until you guess the correct number

# author: gerry callaghan

number_to_guess = 30

guess = int(input("Please guess the correct number: "))

while guess != number_to_guess:
    if guess < number_to_guess:
        print(f"Too low")
        guess = int(input("Please guess again: "))
    elif guess > number_to_guess:
        print(f"Too high")    
        guess = int(input("Please guess again: "))
        

print(f"Well done! Yes the number was {number_to_guess}")  

# Get the program to generate a random number between 0 and 100 for you to guess

import random
second_number_to_guess = random.randrange(1, 100)

guess = int(input("Please guess another number between 1 and 100: "))

while guess != second_number_to_guess:
    if guess < second_number_to_guess:
        print(f"Too low")
        guess = int(input("Please guess again: "))
    elif guess > second_number_to_guess:
        print(f"Too high")    
        guess = int(input("Please guess again: "))
        

print(f"Well done! Yes the number was {second_number_to_guess}")  


