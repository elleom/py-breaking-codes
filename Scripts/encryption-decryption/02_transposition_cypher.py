#!/usr/bin/env python

# Transposition Cypher steps

# Count the number of characters in the message and the key.
# Draw a row of a number of boxes equal to the key (for example, 8 boxes
# for a key of 8).
# Start filling in the boxes from left to right, entering one character
# per box.
# When you run out of boxes but still have more characters, add another
# row of boxes.
# When you reach the last character, shade in the unused boxes in the
# last row.
# Starting from the top left and going down each column, write out the
# characters. When you get to the bottom of a column, move to the next
# column to the right. Skip any shaded boxes. This will be the ciphertext.
import argparse
import textwrap


def main():
    arguments = parse_arguments()
    process_data(arguments)


def process_data(arguments):
    mode = arguments.encrypt
    message = arguments.message
    key = arguments.key

    print(key, message, mode)


def parse_arguments():
    parser = argparse.ArgumentParser(description="TRANSPOSITION CYPHER TOOL",
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     epilog=textwrap.dedent("""Example:
        python 02_transposition_cypher [--encrypt] --message "MESSAGE" --key 8
        NOTE => default mode is decrypt"""))
    parser.add_argument("-m", "--message", help="Message to be encrypted/decrypted")
    parser.add_argument("-e", "--encrypt", action="store_true", help="=> tool's defaultMode = decrypt")
    parser.add_argument("-k", "--key", help="Key for the transposition")
    return parser.parse_args()


if __name__ == "__main__":
    main()