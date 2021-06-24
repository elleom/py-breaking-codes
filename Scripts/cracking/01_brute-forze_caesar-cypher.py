#!/usr/bin/env python

import argparse
import textwrap


class MessageProcessor:
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    def __init__(self, args):
        self.args = args

    def process_message(self):
        print('proccess message')

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