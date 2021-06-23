#!/usr/bin/env python

# Reverse Cypher
# cracking codes with python

def reverse_cypher(input_message):
    translated = ''

    i = len(input_message) - 1
    while i >= 0:
        translated = translated + input_message[i]
        i -= 1
    print(translated)


def user_input():
    user_msg = input('[+] Write message > ')
    return user_msg


if __name__ == '__main__':
    message = user_input()
    reverse_cypher(message)



