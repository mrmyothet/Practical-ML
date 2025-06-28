import random

secret_number = random.randint(1, 10)
print("I've thought of a number between 1 and 10. Can you guess it?")

while True:
    try:

        guess = int(input("Your guess: "))

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"You got it! The number was {secret_number}.")
            break

    except ValueError:
        print("Oops! That's not a number. Please, enter a number between 1 and 10.")
