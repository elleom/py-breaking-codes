#!/usr/bin/env python

# Caesar Cypher

import paperclip

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
    get_user_input()