# Password generator that asks user for input and returns a random password.

import random
import string


def generate_password(length, min_digits, min_special_chars):
    uppercase_letters = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
    lowercase_letters = 'abcdefghijkmnopqrstuvwxyz'
    digits = '0123456789'
    special_chars = '!@#$%^&*'

    if min_digits + min_special_chars > length:
        raise ValueError(
            "Digits plus special characters exceed the password length.")

    if min_digits < 0 or min_special_chars < 0 or length <= 0:
        raise ValueError("All values must be positive integers.")

    password = []
    password.extend(random.choices(digits, k=min_digits))
    password.extend(random.choices(special_chars, k=min_special_chars))

    remaining_length = length - min_digits - min_special_chars
    all_letters = uppercase_letters + lowercase_letters
    password.extend(random.choices(all_letters, k=remaining_length))

    while True:
        random.shuffle(password)
        if all(password[i] != password[i + 1] for i in range(len(password) - 1)):
            break

    return ''.join(password)


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError("Value must be non-negative.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive integer.")


def main():
    print("Random Password Generator")

    length = get_positive_integer("Enter the total length of the password: ")
    min_digits = get_positive_integer("Enter the minimum number of digits: ")
    min_special_chars = get_positive_integer(
        "Enter the minimum number of special characters: ")

    while True:
        try:
            password = generate_password(length, min_digits, min_special_chars)
            print("Generated Password:", password)
        except ValueError as e:
            print("Error:", e)
            continue

        again = input("Generate new password? (Y/N): ").strip().lower()
        if again not in ['yes', 'y']:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
