# Importing random tool
import random

# defining the function for our random number guesser app
def random_number_guesser():

    # generating the secret number
    noct_secret_number = random.randint(1,20)

    # number of guesses allowed
    guess = 5
    guess_limit = 0

    print("Welcome to the number guessing game.")
    print(f"You are allowed {guess} guess chances.")

    while True:
        if guess == guess_limit:
            print("Game over. You exhausted all guess chances.")
            print(f"The secret number was, {noct_secret_number}")

        try:
            user_guess = int(input("Guess the secret number (1-100): "))

            if user_guess < 1 or user_guess > 20:
                print("Guess a number between 1 and 20")
                continue

            if user_guess > noct_secret_number:
                print("Oops! Your guess was high, try again.")
            elif user_guess < noct_secret_number:
                print("Oops! Your guess was low, try again.")
            else:
                print(f"Yippee, your guess {user_guess} was correct.")
                return

            # reducing guess chances after every invalid guess
            guess -= 1
            print(f"You have {guess} guess chances left.")

        except ValueError:
            print("Enter a valid number.\n")

random_number_guesser()

