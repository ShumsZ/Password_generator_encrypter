import csv
import random


def pass_create():
    user_input = input('Create new password: ')

    commonly_used_passwords = []

    with open('common_passwords.csv') as cpfile:
        cp_reader = csv.reader(cpfile)

        for i in cp_reader:
            for x in i:
                commonly_used_passwords.append(x)

    def check():
        new_pass = ''
        for password in commonly_used_passwords:
            if user_input != password:
                new_pass = user_input

            else:
                print(
                    'Your password is identical to a very commonly used password and therefore easy to guess. Do better!')
                return None
        return new_pass

    user_input_pass = check()
    return user_input_pass


def pass_gen():
    # double the number occurrences to increase their chances of being selected by random.choice
    variables = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z',
                 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z',
                 '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                 '£', '$', '%', '&', '!', '*', '£', '$', '%', '&', '!', '*']

    chars = int(input('Enter required number of characters for your password (8 or above is recommended): '))

    password = ""
    warning = "WARNING: YOUR PASSWORD MAY BE TOO SHORT"

    for i in range(1, chars + 1):
        password += random.choice(variables)

    if len(password) <= 8:
        print(warning)
    return password


starting_q = input(
    'Would you like to make your own password or generate one: C to create own password; G to generate one: ')

if starting_q == 'C':
    new_password = pass_create()
elif starting_q == 'G':
    new_password = pass_gen()
else:
    new_password = ''

print(new_password)

dec_key = {"A": "Q", "B": "W", "C": "E", "D": "R", "E": "T", "F": "Y", "G": "U", "H": "I", "I": "O", "J": "P", "K": "A",
           "L": "S", "M": "D", "N": "F", "O": "G", "P": "H", "Q": "J", "R": "K", "S": "L", "T": "Z", "U": "X", "V": "C",
           "W": "V", "X": "B", "Y": "N", "Z": "M",
           "a": "q", "b": "w", "c": "e", "d": "r", "e": "t", "f": "y", "g": "u", "h": "i", "i": "o", "j": "p", "k": "a",
           "l": "s", "m": "d", "n": "f", "o": "g", "p": "h", "q": "j", "r": "k", "s": "l", "t": "z", "u": "x", "v": "c",
           "w": "v", "x": "b", "y": "n", "z": "m"}

# Swaps out the keys for values in order to facilitate encryption. This only works because the keys AND values are
# all unique characters.
enc_key = dict((v, k) for k, v in dec_key.items())


def encrypt():
    # user_input_en = list(input("Enter encryption here: "))

    encrypted_version = ""
    if new_password is None:
        return None

    for element in new_password:

        if element in dec_key:
            encrypted_version += dec_key[element]

        else:
            encrypted_version += element

    return encrypted_version


def decrypt():
    user_input_de = list(input("Enter code to decrypt here: "))

    decrypted_version = ""

    for element in user_input_de:

        if element in enc_key:
            decrypted_version += enc_key[element]

        else:
            decrypted_version += element
    return decrypted_version


encrypted_password = encrypt()
print(encrypted_password)

dec_q = input('Would you like to decrypt a password? (Y for yes, any other letter for no): ')
if dec_q == 'Y':
    decrypted_password = decrypt()
    print(decrypted_password)
else:
    print('No other services to offer at this time :)')
