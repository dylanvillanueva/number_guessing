import random
import art

random_num = random.randint(0, 101)

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == 'easy':
    total_guesses = 10
else:
    total_guesses = 5

guess_number = True

while guess_number:
    print("Guess again.")
    print(f"You have {total_guesses} attempts remaining to guess the number.")

    user_guess = int(input("Make a guess: "))

    if user_guess == random_num:
        print(f"You got it! The answer was {random_num}.")
        guess_number = False
    elif user_guess > random_num:
        print("Too high.")
        total_guesses -= 1
    else:
        print("Too low.")
        total_guesses -= 1

    if total_guesses == 0:
        print("You've run out of guesses, you lose.")
        guess_number = False
