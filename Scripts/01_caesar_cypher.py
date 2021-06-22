#!/usr/bin/env python

# Caesar Cypher
import textwrap

import paperclip
import argparse

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


def decrypt_message(message, key, mode):
    decrypted_message = ''
    for symbol in message:
        # Note: only symbos within SYMBOLS const can be traced
        if symbol in SYMBOLS:
            symbol_index = SYMBOLS.find(symbol)

            # performs encrypt/decrypt
            if mode == 'encrypt'


def get_user_input():
    encrypted_message = input('[+] Introduce encrypted message>')
    while True:
        try:
            message_key = int(input('[+] Introduce the key'))
            break
        except ValueError:
            print('Introduce a number, please')


if __name__ == '__main__':
    mode = ''
    parser = argparse.ArgumentParser(description='CAESAR CYPHER TOOL',
                                     # Help Message Formatter
                                     # which retains any formatting in description
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     epilog=textwrap.dedent('''Example;
                                     01_caesar_cypher.py -e encrypt [message] \ndefault = decrypt'''))
    parser.add_argument('-e', '--encrypt', action='store_true',  help='Encrypts the given message')
    parser.add_argument('-k', '--key', help='Transmuting key use to encrypt/decrypt')
    args = parser.parse_args()

    #todo finish
