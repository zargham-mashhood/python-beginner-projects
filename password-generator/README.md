# Password Generator (CLI)

A small command-line password generator written in Python.

## What it does

- Generates a random password of a length you choose (4–64 characters)
- Uses letters, digits and symbols (symbols optional)
- Uses Python's `secrets` module — made for security-sensitive randomness

## How to run

```bash
python3 password_generator.py
```

## What I learned

- The `secrets` module vs the `random` module
- Working with `string` constants (`ascii_letters`, `digits`, `punctuation`)
- Input validation and sensible defaults
