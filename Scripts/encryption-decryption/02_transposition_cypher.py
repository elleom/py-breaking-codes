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
    arguments = check_arguments(arguments)
    processed_message = process_message(arguments[0], arguments[1], arguments[2])
    print(processed_message)


def check_arguments(arguments):
    # if mode not specified then false
    mode = arguments.encrypt

    # checks for the message within the call to the script, if not then prompts
    if not arguments.message:
        message = input('[-] Message not found, please introduce the message to encrypt/decrypt\n>')
    message = arguments.message

    # check for a key, if not then prompts
    if not arguments.key:
        key = int(input("[-] Introduce the key integer\n"))
    key = int(arguments.key)
    # packs a tuple
    return mode, message, key


def process_message(mode, message, key):
    processed_message = ''
    print(message, key, mode)

    return processed_message


def parse_arguments():
    parser = argparse.ArgumentParser(description="TRANSPOSITION CYPHER TOOL",
                                     # Help Message Formatter
                                     # which retains any formatting in description
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