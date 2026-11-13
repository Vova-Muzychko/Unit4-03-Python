#!/usr/bin/env python3
# Created by: Vova
# Created on: November 13 2026
# This program asks for a whole number and displays the square of every number from 0 up to that number.


def main():
    # Get user input as a string
    user_string = input("Enter a whole number: ")
    print("")

    # Try to convert input to an integer and run the loop
    try:
        user_num = int(user_string)

        # Check if the number is negative
        if user_num < 0:
            print("Please enter a positive whole number.")
        else:
            # Calculate and display squares from 0 to user_num
            for counter in range(user_num + 1):
                answer = counter**2
                print(f"{counter}² = {answer}")

    except Exception:
        # Catch invalid text or decimal inputs
        print(f"{user_string} is not a valid whole number.")

    print("\nDone.")


if __name__ == "__main__":
    main()
