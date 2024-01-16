import random

def get_guess():
    while True:
        guess = input("Guess a three-digit number: ")
        if guess.isdigit() and len(guess) == 3:
            return guess
        print("Please enter a valid three-digit number.")

def get_hints(guess, secret_code):
    output = ""
    for i, n in enumerate(guess):
        if n == secret_code[i]:
            output += "Bullseye "
        elif n in secret_code:
            output += "Off-target "
        else:
            output += "Null "
    return output

def generate_secret_code():
    return [str(random.randint(0, 9)) for _ in range(3)]

def guessing_game():
    secret_code = generate_secret_code()
    max_guess = 10
    current_guess = 0

    print("Welcome to 'Conundrum Code'. Try to guess the three digit number.\n")

    print("Here are some clues: ")
    print("When I say 'Off-target' that means one of your digits is correct but in the wrong position.")
    print("When I say 'Bullseye' that means one of your digits is correct but in the right position.")
    print("When I say 'Null' that means one of your digits is incorrect.")

    while current_guess < max_guess:
        guess = get_guess()
        hints = get_hints(guess, secret_code)

        if hints == "Bullseye Bullseye Bullseye ":
            print("You got it!")
            restart = input("Do you want to play again? (y/n)").lower()
            if restart == "n":
                print("Thank you for playing.")
                break
            else:
                current_guess = 0
                secret_code = generate_secret_code()
                continue
        else:
            print(hints)

        current_guess += 1

        if current_guess == max_guess:
            print("You lost! The code was", secret_code)
            restart = input("Do you want to play again? (y/n)").lower()
            if restart == "n":
                print("Thank you for playing.")
                break
            else:
                current_guess = 0
                secret_code = generate_secret_code()

guessing_game()
