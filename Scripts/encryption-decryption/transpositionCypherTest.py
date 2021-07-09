#!/usr/bin/env python

# Transposition Cipher Test
# from cracking codes

import random
import sys
from transpositionCypher import encrypt_message as encrypt
from transpositionCypher import decrypt_message as decrypt


def main():
    # sets seed to a static value
    # see https://docs.python.org/3.9/library/random.html#random.seed
    random.seed(42)

    for i in range(20):  # run n tests
        # generate random messages to test
        message = 'ABCDEFGHIGKLMOPQRSTUVWXYZ' * random.randint(4, 40)  # min 4, max 40

        # convert message to list and shuffles it
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)  # converts back to string

        print('[*] Test #%s: "%s..."' % (i + 1, message[:50]))

        for key in range(1, int(len(message)/2)):
            encrypted_message = encrypt(message, key)  # generates ciphertext
            decrypted_message = decrypt(encrypted_message, key)  # generates plaintext

            if decrypted_message != message:
                print('[!] Mismatch with key %s and message %s.' % (key, message))
                print('[!] Decrypted as %s' % decrypted_message)
                print('[!] Failed, exiting...')
                sys.exit()

    print('[+] All test passed')


if __name__ == '__main__':
    main()






