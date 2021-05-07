#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: May 2021
# This program guesses your number
#    with numbers inputted from the user

import random


def main():
    # This function guesses your number

    # input
    guessed_string = input("Enter the number between 0 - 9: ")
    random_number = random.randint(0, 9)

    # process/output
    if guessed_string == random_number:
        print("You guessed correct!")
    try:
        guessed_number = int(guessed_string)
    except Exception:
        print("{} is not an integer".format(guessed_string))
    else:
        print("Incorrect, the number was {}".format(random_number))
    finally:
        print("Thanks for playing")
    print("\nDone")


if __name__ == "__main__":
    main()
