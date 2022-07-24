#!/usr/bin/env python

import sys
import os
import textwrap
import time
import argparse
from transpositionCypher import decrypt_message as decrypt
from transpositionCypher import encrypt_message as encrypt


def main():

    arguments = parse_args()

    if not arguments.file:
        print('[!] Input File not provided')
        print('[!] Closing... run --help for instructions')
        sys.exit()
    if not arguments.key:
        print('[!] Key not provided')
        print('[!] Closing... run --help for instructions')
        sys.exit()

    print('[*] Starting process', end='', flush=True)
    time.sleep(0.5)
    for symbol in '...':
        print(symbol, end='', flush=True)
        time.sleep(0.5)
    print('\n[*] Parsing arguments', end='', flush=True)
    for symbol in '...':
        print(symbol, end='', flush=True)
        time.sleep(0.5)
    print('\n[*] Adding some more drama to the script', end='', flush=True)
    for symbol in '...':
        print(symbol, end='', flush=True)
        time.sleep(1)

    run(arguments)


def run(arguments):
    output_file_path = ''

    # create output file
    input_file_path = arguments.file
    if not arguments.output and arguments.encrypt:
        output_file_path = arguments.file[:-3] + 'encrypted.txt'
    elif not arguments.output and not arguments.encrypt:
        output_file_path = arguments.file[:-3] + 'decrypted.txt'
    else:
        output_file_path = arguments.output

    # call process procedure
    process_file(input_file_path, output_file_path, arguments.encrypt, arguments.key)


def process_file(input_file, output_file, do_encrypt, key):
    if not os.path.exists(input_file):
        print('\n[!] Input file %s not found . Quitting' % input_file)
        sys.exit()
    if os.path.exists(output_file):
        print('\n[!] Output file %s already exists, this will overwrite it' % output_file)
        response = input('[?] (C)ontinue or (Q)uit?\n>')
        if not response.lower().startswith('c'):
            sys.exit()

    # read in the message from input file
    input_file_object = open(input_file)
    file_content = input_file_object.read()
    input_file_object.close()

    output_file_content = open(output_file, 'w')

    if do_encrypt:
        encrypted_content = encrypt(file_content, int(key))
        print("\n\n[*] Printing encrypted content...\n")
        print(encrypted_content)
        output_file_content.write(encrypted_content)

    elif not do_encrypt:
        decrypted_content = decrypt(file_content, int(key))
        print("\n\n[*] Printing decrypted content...\n")
        print(decrypted_content)
        output_file_content.write(decrypted_content)


def parse_args():
    parser = argparse.ArgumentParser(description='Transposition Cypher encrypt/decrypt - FILES',
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     epilog=textwrap.dedent("""Example:
        python transpositionCypherFile [--encrypt] --file "/path/to/file" --output-file "/path/to/file"  --key 8
        NOTE => default mode is decrypt"""))
    parser.add_argument('-f', '--file', required=True, help='Text file to be encrypted/decrypted')
    parser.add_argument('-e', '--encrypt', action='store_true', help='Default mode is decrypt')
    parser.add_argument('-k', '--key', required=True, help='Message Key for encrypt/decrypt')
    parser.add_argument('-o', '--output', help='Output file path or filename')
    return parser.parse_args()


if __name__ == '__main__':
    main()
