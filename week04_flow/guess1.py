# this program prompts you to continually guess a number until you guess the correct number

# author: gerry callaghan

number_to_guess = 30

guess = int(input("Please guess the correct number: "))

while guess != number_to_guess:
    print(f"Wrong")
    guess= int(input("Please guess again: "))

print(f'Well done! Yes, the number was {number_to_guess} ')
