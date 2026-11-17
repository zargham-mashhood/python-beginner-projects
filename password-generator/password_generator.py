"""Password generator (command line).

Generates a random password of a chosen length using letters, digits
and symbols. Uses the `secrets` module, which is designed for
security-sensitive randomness (better than `random` for passwords).

Run:  python3 password_generator.py
"""

import secrets
import string


def generate_password(length=12, use_symbols=True):
    """Build a random password of the given length."""
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation if use_symbols else ""

    alphabet = letters + digits + symbols
    if not alphabet:
        raise ValueError("No characters available for the password.")

    return "".join(secrets.choice(alphabet) for _ in range(length))


def main():
    print("--- Password Generator ---")

    try:
        length = int(input("Password length (default 12): ") or 12)
    except ValueError:
        print("Not a number — using length 12.")
        length = 12

    if length < 4:
        print("Too short — using length 4.")
        length = 4
    elif length > 64:
        print("Too long — using length 64.")
        length = 64

    symbols_answer = input("Include symbols? (y/n, default y): ").strip().lower()
    use_symbols = symbols_answer != "n"

    password = generate_password(length, use_symbols)
    print(f"\nYour password: {password}")
    print("Tip: store it in a password manager, not in a plain text file.")


if __name__ == "__main__":
    main()
