from primes import random_prime

def gcd(a, b):
    """Finds the greatest common divider of two numbers

    Args:
        a (int): first number
        b (int): second number

    Returns:
        int: the greatest common divider of given numbers
    """

    if (a < 1 or b < 1):
        print("Error: Cislo 'a' aj cislo 'b' musia byt vacsie ako 0!")
        return -1
    
    while b != 0:
        temp = a
        a = b
        b = temp % b

    return a


def find_indivisible_to(prime_len, num):
    """Finds an indivisible number to a number passed in

    Generates a prime that is lower than passed number in loop until
    it really is indivisible with passed number.

    Args:
        prime_len (int): length of prime that will be generated, must be lower than len(num)
        num (int): number to find indivisible number to

    Returns:
        int: required indivisible number
    """

    while True:
        candidate = random_prime(prime_len)
        if num % candidate != 0:
            return candidate


def str_to_bin(string):
    """Converts string to binary its binary representation

    Args:
        string (str): string to convert

    Returns:
        str: string of ones and zeros
    """

    encoded_str = string.encode()
    encoded_str_hex = encoded_str.hex()
    binary_str = bin(int(encoded_str_hex, 16))[2:]

    return binary_str
    

def bin_to_str(bin_data):
    """Converts binary to utf8 string

    Args:
        bin_data (str): string of ones and zeros

    Returns:
        str: converted utf8 string
    """

    hex_data = "{0:0>4X}".format(int(bin_data, 2))
    bytes_str = bytes.fromhex(hex_data)
    decoded_str = bytes_str.decode()

    return decoded_str


def split_to_groups(data, group_len):
    return [data[i:i+group_len] for i in range(0, len(data), group_len)]