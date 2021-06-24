#!/usr/bin/env python

import argparse
import textwrap


class MessageProcessor:
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    def __init__(self, args):
        self.args = args

    def process_message(self):
        for key in range(len(self.SYMBOLS)):
            translated_message = ''  # blanks the message after each iteration
            for symbol in self.args.message:
                if symbol in self.SYMBOLS:
                    symbol_index = self.SYMBOLS.find(symbol)
                    translated_index = symbol_index - key

                    #  handle wraparound
                    if translated_index < 0:
                        translated_index = translated_index + len(self.SYMBOLS)
                    # append symbol
                    translated_message += self.SYMBOLS[translated_index]
                else:
                    # append raw symbol => symbol not in self.SYMBOLS
                    translated_message += symbol
            print('Key #%s: %s' % (key, translated_message))

    def get_user_input(self):
        if not self.args.message:
            self.args.message = input('Message not introduced, please type>')

    def run(self):
        self.get_user_input()
        self.process_message()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CAESAR CYPHER - brute-forcing tool',
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     epilog=textwrap.dedent('''Example:
    python 01_brute-force_caesar-cypher.py -m " [message] " '''))
    parser.add_argument('-m', '--message', help='Message to be decrypted => ex: " this is a message" ')
    user_input = parser.parse_args()
    processor = MessageProcessor(user_input)
    processor.run()