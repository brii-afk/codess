import random


def guessing_game():
    lower_bound = 1
    upper_bound = 100

    random_number = random.randint(lower_bound, upper_bound)

    print(f"Welcome to the guessing game! Guess a number between {lower_bound} and {upper_bound}.")

    attempts = 0

    while True:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)

        attempts += 1

        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break


# Run the guessing game
guessing_game()

