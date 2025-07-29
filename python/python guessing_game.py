import random

def guessing_game():
    print("Welcome! I am thinking of a number between 1 and 50.")
    print("Can you guess what it is?")

    secret_number = random.randint(1, 50)
    attempts = 0

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} tries.")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    guessing_game()
