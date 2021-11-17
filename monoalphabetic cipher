plaintext = input("enter the plaintext: ").lower()
ciphertext = input("enter the ciphertext: ").lower()
valid_letters = "abcdefghijklmnopqrstuvwxyz"
user_key = input("enter the key: ").lower()
key = ""

new_string = ""


for char in plaintext:
    if char in valid_letters:
        new_string += char

for char in user_key:
    if char in valid_letters:
        if char not in key:
            key += char

for char in valid_letters:
    if char not in key:
        key += char


def encrypt():
    index_values = [valid_letters.index(char) for char in new_string]
    return "".join(key[indexKey] for indexKey in index_values)


def decrypt():
    index_values = [key.index(char) for char in ciphertext]
    return "".join(valid_letters[indexKey] for indexKey in index_values)


ciphertext = encrypt()
print("encrypted message: ", ciphertext)
original = decrypt()
print("decrypted message: ", original)
