#!/usr/bin/env python3

# To use, type this code:
# import detectEnglish
# detectEnglish.isEnglish(someString) # Returns True or False
# (There must be a "dictionary_file.txt" file in this directory with all
# English words in it, one word per line.


UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPER_LETTERS + UPPER_LETTERS.lower() + ' \t\n'


def load_dictionary():
    dictionary_file = open('../assets/words.txt')
    dictionary_words = {}  # creates a dictionary to store the key value pairs
    for word in dictionary_file.read().split('\n'):
        dictionary_words[word] = None
    dictionary_file.close()
    return dictionary_words


DICTIONARY_WORDS = load_dictionary()


