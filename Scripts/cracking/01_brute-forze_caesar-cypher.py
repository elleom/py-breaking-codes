#!/usr/bin/env python

import argparse
import textwrap


class MessageProcessor:
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    def __init__(self, args):
        self.args = args

    def process_message(self):
        print('proccess message')

    def run(self):
        self.process_message()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CAESAR CYPHER - brute-forcing tool',
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     epilog=textwrap.dedent('''Example:
    python 01_brute-force_caesar-cypher.py -m " [message] " '''))
    parser.add_argument('-m', '--message', help='Message to be decrypted => ex: " this is a message" ')