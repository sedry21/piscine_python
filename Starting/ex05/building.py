#!/usr/bin/env python3
"""Count character types in a string."""

import sys
import string


def count_characters(text):
    """
    Count different character types in a string.

    Args:
        text: The string to analyze

    Returns:
        A dictionary with counts of each character type
    """
    counts = {
        'upper': sum(1 for c in text if c.isupper()),
        'lower': sum(1 for c in text if c.islower()),
        'punctuation': sum(1 for c in text if c in string.punctuation),
        'digits': sum(1 for c in text if c.isdigit()),
        'spaces': text.count(' ')
    }
    return counts


def main():
    """Main function to handle command line arguments and display results."""
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return

    if len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        text = input("What is the text to count?\n")

    counts = count_characters(text)
    total = len(text)

    print(f"The text contains {total} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punctuation']} punctuation marks")
    print(f"{counts['spaces']} spaces")
    print(f"{counts['digits']} digits")


if __name__ == "__main__":
    main()
