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
    user_input_en = list(input("Enter encryption here: "))

    encrypted_version = ""

    for element in user_input_en:

        if element in dec_key:
            encrypted_version += dec_key[element]

        else:
            encrypted_version += element

    print(encrypted_version)


def decrypt():
    user_input_de = list(input("Enter code to decrypt here: "))

    decrypted_version = ""

    for element in user_input_de:

        if element in enc_key:
            decrypted_version += enc_key[element]

        else:
            decrypted_version += element
    print(decrypted_version)


dividing_q = input("Would you like to encrypt(E) or decrypt(D)? : ")

if dividing_q == "E":
    encrypt()
else:
    decrypt()
