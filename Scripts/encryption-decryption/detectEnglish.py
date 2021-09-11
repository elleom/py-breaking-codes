#!/usr/bin/env python3

# To use, type this code:
# import detectEnglish
# detectEnglish.isEnglish(someString) # Returns True or False
# (There must be a "dictionary_file.txt" file in this directory with all
# English words in it, one word per line.
import argparse
import textwrap

UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPER_LETTERS + UPPER_LETTERS.lower() + ' \t\n'


def load_dictionary():
    dictionary_file = open('../assets/words.txt')
    dictionary_words = {}  # creates a dictionary to store the key value pairs
    for word in dictionary_file.read().split('\n'):  # each lines finishes with \n on the word file
        dictionary_words[word] = None
    dictionary_file.close()
    return dictionary_words


DICTIONARY_WORDS = load_dictionary()


def remove_non_letters(message):
    letters_only = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            letters_only.append(symbol)
    return ''.join(letters_only)


def get_dictionary_count(message):
    f = open(message, "r")
    message = f.read()
    message = message.upper()
    message = remove_non_letters(message)
    possible_words = message.split()


def parse_arguments():
    parser = argparse.ArgumentParser(description="DECRYPTED MESSAGE LANGUAGE DETECTOR",
                                     # Help message formater
                                     # retains format in description
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     epilog=textwrap.dedent("""Example:
        python detectEnglish --file "path" """))
    parser.add_argument("-f", "--file", dest="file_path", help="Encrypted document path")
    return parser.parse_args()


def main():
    arguments = parse_arguments()
    get_dictionary_count(arguments.file_path)



if __name__ == "__main__":
    main()
