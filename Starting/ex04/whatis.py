#!/usr/bin/env python3
"""Script to check if a number is even or odd."""

import sys


def check_number(num_str):
    """
    Check if a number is even or odd.

    Args:
        num_str: String representation of the number to check

    Raises:
        AssertionError: If the argument is not an integer

    Returns:
        str: Message indicating if the number is even or odd
    """
    try:
        num = int(num_str)
    except ValueError:
        raise AssertionError("argument is not an integer")

    if num % 2 == 0:
        return "I'm Even."
    else:
        return "I'm Odd."


def main():
    """Main function to handle command line arguments and display result."""
    if len(sys.argv) == 1:
        return

    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return

    try:
        result = check_number(sys.argv[1])
        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
