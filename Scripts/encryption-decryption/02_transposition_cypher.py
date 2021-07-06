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
import math
import textwrap


def main():
    arguments = parse_arguments()
    arguments = check_arguments(arguments)
    processed_message = process_message(arguments[0], arguments[1], arguments[2])
    print(processed_message)


def check_arguments(arguments):
    # checks for the message within the call to the script, if not then prompts
    if not arguments.message:
        message = input('[-] Message not found, please introduce the message to encrypt/decrypt\n>')
    else:
        message = arguments.message

    # check for a key, if not then prompts
    if not arguments.key:
        key = int(input("[-] Introduce the key integer\n"))
    else:
        key = int(arguments.key)

    # if mode not specified then false
    mode = arguments.encrypt

    # packs a tuple
    return mode, message, key


def process_message(encrypt, message, key):  # encrypt refers to encrypt/decrypt mode
    processed_message = ''

    if encrypt:
        processed_message = encrypt_message(message, key)
    else:
        processed_message = decrypt_message(message, key)

    return processed_message


def encrypt_message(message, key):
    ciphertext = [''] * key  # creates n (n = to key/columns) amount of list elements

    for column in range(key):
        current_index = column

        # keep looking until current_index goes past the message length
        while current_index < len(message):
            # place the char at current_index in message at the end of
            # the current column in the ciphertext list
            ciphertext[column] += message[current_index]

            # move current index n (key) amount of spaces
            current_index += key

            # convert ciphertext list into a single string and return

    return ''.join(ciphertext)


def decrypt_message(message, key):
    # The decrypt func simulates columns and rows of the grid the plain text is written on by using a list of strings,

    # number of columns in the transposition grid
    num_columns = int(math.ceil(len(message) / float(key)))
    num_rows = key
    num_shaded_boxes = (num_columns * num_rows) - len(message)

    plaintext = [''] * num_columns
    row = 0
    column = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1  # points to next column

        # if there s no more symbols or we are at a shadow box then go back to first column
        # and the next row
        if (column == num_columns) or (column == num_columns - 1
                                       and row >= num_rows - num_shaded_boxes):
            column = 0
            row += 1

    return ''.join(plaintext)


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
