"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

"""

import random

# Function to format my intro/welcome message
def format_title(text):
    return text.center(70, '*')

# Function to make sure guesses are valid numbers.
def guess_validator(input_text):
    while True:
        try:
            guess = int(input(input_text))
            if guess >= 1 and guess <= 10:
                break
            else:
                print('Your guess must be a number between 1 and 10!')
        except ValueError:
            print('Your guess must be a number!')
            continue
    return guess

# The main body of the game.
def start_game(high_score):
    
    # Display an intro/weclome message to the player
    print(format_title(''))
    print(format_title('-= Number Guessing Game =-'))
    if high_score < 11:
        print(format_title(f'   HIGH SCORE : {high_score}   '))
    else:
        print(format_title(f'   HIGH SCORE : --  '))
    input(format_title(' Press any key to continue '))
    
    # Store a random number as the answer/solution
    correct_number = random.randint(1, 10)
    print('\n\nA random number has been generated between 1 and 10!')
    
    #Prompt the player for an initial guess and make sure it is a valid number.
    guess = guess_validator('Try to guess the number!: ')
    
    attempts = 1
    while guess != correct_number:
        attempts += 1
        if guess > correct_number:
            guess = guess_validator('Too high...guess again: ')
        else:
            guess = guess_validator('Too Low...guess again: ')
        
    # Once the guess is correct, stop looping, inform the user they "Got it"
    #   and show how many attempts it took them to get the correct number.
        
    print(f'\n{correct_number} is the correct number! You got it in {attempts} trys.')
     
    # Keep track of and display the users high score.
    if attempts < high_score:
        high_score = attempts
        print(f'You set a new high score of {high_score}!')
    else:
        print(f'Current high score is {high_score}.')
        
    
    # Ask if the user would like to play again. Replay if yes and display ending message if no.
    while True:
        retry = input('\nWould you like to play again? Y/N ')
        if retry.lower() == 'y' or retry.lower() == 'yes':
            start_game(high_score)
            break
        elif retry.lower() == 'n' or retry.lower() == 'no':
            print(format_title(' Thank you for playing! '))
            break
        else:
            print("Please enter 'Y' for Yes or 'N' for No")
   
   
# Kick off the program by calling the start_game function.
start_game(11)