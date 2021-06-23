#!/usr/bin/env python

# Caesar Cypher
import textwrap
import argparse
import paperclip


class MessageProcessor:
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    def __init__(self, args):
        self.args = args

    def process_message(self):
        message = ''
        for symbol in self.args.message:
            # Note: only symbols within SYMBOLS const can be traced
            if symbol in self.SYMBOLS:
                symbol_index = self.SYMBOLS.find(symbol)

                # performs encrypt/decrypt
                if self.args.encrypt:
                    encrypted_index = symbol_index + self.args.key
                else:
                    encrypted_index = symbol_index - self.args.key

                # handle rollover if needed
                if encrypted_index >= len(self.SYMBOLS):
                    encrypted_index = encrypted_index - len(self.SYMBOLS)
                elif encrypted_index < 0:
                    encrypted_index = encrypted_index + len(self.SYMBOLS)

                message = message + self.SYMBOLS[encrypted_index]
            else:
                # message symbol without enc/dec
                message = message + symbol
        return message

    def run(self):
        self.get_user_input()
        processed_message = self.process_message()
        paperclip.copy(processed_message) # adds result to clipboard
        self.print_message(processed_message)


    def get_user_input(self):
        try:
            if not self.args.key:
                self.args.key = int(input('[*] Key not specified, please provide key>'))
            # transforms string args to int for processing
            self.args.key = int(self.args.key)
            if not self.args.message:
                self.args.message = input('[*] Message not specified, please provide message>')
        except KeyboardInterrupt:
            print('[-] Program quited\n')

    def print_message(self, message):
        print(message)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CAESAR CYPHER TOOL',
                                     # Help Message Formatter
                                     # which retains any formatting in description
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     epilog=textwrap.dedent('''Example;
                                                 01_caesar_cypher.py -e encrypt [message] => default = decrypt'''))
    parser.add_argument('-e', '--encrypt', action='store_true', help='Encrypts the given message')
    parser.add_argument('-k', '--key', help='Transmuting key use to encrypt/decrypt')
    parser.add_argument('-m', '--message', help='Message to be encrypted/decrypted => ex: " this is a message" ')
    user_input = parser.parse_args()
    processor = MessageProcessor(user_input)
    processor.run()




