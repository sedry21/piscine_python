#!/usr/bin/env python3
"""Filter words by length from a string."""

import sys


def main():
    """Filter words from a string that are longer than N characters."""
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        return

    try:
        string_arg = sys.argv[1]
        n_arg = int(sys.argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        return

    words = string_arg.split()
    result = [word for word in words if (lambda w: len(w) > n_arg)(word)]

    print(result)


if __name__ == "__main__":
    main()
