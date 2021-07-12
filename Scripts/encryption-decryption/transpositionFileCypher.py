#!/usr/bin/env python

import sys
import os
import textwrap
import time
import argparse
from transpositionCypher import decrypt_message as decrypt
from transpositionCypher import encrypt_message as encrypt


def main():
    print('something')


def parse_args():
    parser = argparse.ArgumentParser(description='Transposition Cypher encrypt/decrypt - FILES',
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     epilog=textwrap.dedent("""Example:
        python transpositionCypherFile [--encrypt] --filepath "/path/to/file" --output-file "/path/to/file"  --key 8
        NOTE => default mode is decrypt"""))
    parser.add_argument('-f', '--file', help='Text file to be encrypted/decrypted')
    parser.add_argument('-e, --encrypt', action='store_true', help='default mode is decrypt')
    parser.add_argument('-k', '--key', help='Message Key for encrypt/decrypt')
    parser.add_argument('-o, --output-file', help='Output file path or filename')
    return parser.parse_args()


if __name__ == '__main__':
    main()