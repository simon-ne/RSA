"""This test needs to be run from root folder 'rsa_cipher'
"""

import string
import random
import sys, os

# Local imports
sys.path.append(os.path.abspath('.'))
from lib.rsa import RSA

# list of chars to generate a random string from
special_chars = list("ľščťžýáíéň§úřóď")
alphabet = special_chars + list(string.ascii_letters) + list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits) + list(string.hexdigits) + list(string.whitespace) + list(string.punctuation)

def random_string(alphabet):
    """generates a random string of random length from 1 to 50

    Args:
        alphabet (list): list of characters to generate the string from

    Returns:
        str: random string
    """
    
    rand_length = random.randint(1, 50)
    rand_string = ''
    
    for _ in range(rand_length):
        rand_index = random.randint(0, len(alphabet) - 1)
        rand_string += alphabet[rand_index]
    
    return rand_string

# Loop a 1000 iterations of random string test
for i in range(1000):
    # Get new rsa object
    rsa = RSA()

    # Generate a random string
    random_str = random_string(alphabet)

    # Encrypt the generated string and decrypt it
    encrypted = rsa.encrypt(random_str, (rsa.public_key[0], rsa.public_key[1]))
    decrypted = rsa.decrypt(encrypted, (rsa.private_key[0], rsa.private_key[1]))

    # If generated string and decrypted string are not equal
    # print out some debug information
    if random_str != decrypted:
        print(f"{type(random_str)} {len(random_str)} '{random_str}'")
        print(f"{type(decrypted)} {len(decrypted)} '{decrypted}'")

    # Throw error if a mistake is detected
    assert random_str == decrypted

print("ALL TESTS PASSED")