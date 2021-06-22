#!/usr/bin/env python

# Caesar Cypher
import textwrap
import paperclip
import argparse


class MessageProcessor:
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    def __init__(self, args):
        self.args = args

    def process_message(self):
        decrypted_message = ''
        for symbol in self.args.message:
            # Note: only symbols within SYMBOLS const can be traced
            if symbol in self.SYMBOLS:
                symbol_index = self.SYMBOLS.find(symbol)

                # performs encrypt/decrypt

    def run(self):
        if not self.args.key:
            self.args.key = int(input('[*] Key not specified, please provide key>'))
        elif not self.args.message:
            self.args.message = int(input('[*] Message not specified, please provide message>'))
        self.process_message()


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
                                     01_caesar_cypher.py -e encrypt [message] \ndefault = decrypt'''))
    parser.add_argument('-e', '--encrypt', action='store_true',  help='Encrypts the given message')
    parser.add_argument('-k', '--key', help='Transmuting key use to encrypt/decrypt')
    parser.add_argument('-m', '--message', help='Message to be encrypted/decrypted' )
    user_input = parser.parse_args()
    processor = MessageProcessor(user_input)
    processor.run()


