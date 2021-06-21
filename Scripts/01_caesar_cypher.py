#!/usr/bin/env python

# Caesar Cypher
import textwrap

import paperclip
import argparse

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


def decrypt_message(message):
    decrypted_message = ''


def get_user_input():
    encrypted_message = input('[+] Introduce encrypted message>')
    while True:
        try:
            message_key = int(input('[+] Introduce the key'))
            break
        except ValueError:
            print('Introduce a number, please')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CAESAR CYPHER TOOL',
                                     # Help Message Formatter
                                     # which retains any formatting in description
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     epilog=textwrap.dedent('''Example;
                                     01_caesar_cypher.py -e encrypt [message] '''))
    parser.add_argument('-e', '--encrypt', help='Encrypts the given message')
    parser.add_argument('-d', '--decrypt', help='Decrypts the given message')

    #todo finish
