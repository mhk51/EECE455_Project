# plaintext = input("enter the plaintext: ").lower()
# ciphertext = input("enter the ciphertext: ").lower()
valid_letters = "abcdefghijklmnopqrstuvwxyz"
# user_key = input("enter the key: ").lower()








def encrypt_Monoalphabetic(plaintext,inputkey):
    key = ""
    nonalphaChars = []
    new_string = ""
    for i in  range(len(plaintext)):
        char = plaintext[i]
        if char in valid_letters:
            new_string += char
        else:
            nonalphaChars += [(i,char)]

    for char in inputkey:
        if char in valid_letters:
            if char not in key:
                key += char
    
    for char in valid_letters:
        if char not in key:
            key += char
    index_values = [valid_letters.index(char) for char in new_string]
    string =  "".join(key[indexKey] for indexKey in index_values)
    for i in range(len(nonalphaChars)):
        index = nonalphaChars[i][0]
        char = nonalphaChars[i][1]
        string  = string[:index] + char + string[index:]
    return string


def decrypt_Monoalphabetic(ciphertext,inputkey):
    key = ""
    nonalphaChars = []
    new_string = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char in valid_letters:
            new_string += char
        else:
            nonalphaChars += [(i,char)]   #for storing non alphabetical characters and their index
    for char in inputkey:
        if char in valid_letters:
            if char not in key:
                key += char

    for char in valid_letters:
        if char not in key:
            key += char
    index_values = [key.index(char) for char in new_string]
    string = "".join(valid_letters[indexKey] for indexKey in index_values)

    #to place back non alphabet character 
    for i in range(len(nonalphaChars)):
        index = nonalphaChars[i][0]
        char = nonalphaChars[i][1]
        string  = string[:index] + char + string[index:]
    return string


ciphertext = encrypt_Monoalphabetic("the. end","encrypt")
# print("encrypted message: ", "the. end")
# original = decrypt(ciphertext,user_key)
# print("decrypted message: ", original)
