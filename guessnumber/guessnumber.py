import random

def starting_sequence():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if (difficulty == 'hard'):
        attempts = 5
    else:
        attempts = 10
    return attempts

def gameplay(attempts):
    number = random.randint(1, 100)
    print(number)
    while (attempts > 0):
        print(f"You have {attempts} attempts remaining to guess the number")
        guess = int(input ("Make a guess: "))
    
        if (guess > number):
            print("Too high.")
            attempts -= 1
        elif (guess < number):
            print("Too low.")
            attempts -= 1
        elif (guess == number):
            print(f"You got it! The answer was {number}")
            break
        
        if (attempts == 0):
            print("You lost.")
            print(f"The number was {number}.")
        

attempts = starting_sequence()
gameplay(attempts)