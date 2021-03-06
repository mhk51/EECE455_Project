import math
from extended_euclid import extended_euclid
import numpy as np

# plaintext = input("Please input text: ")

# key = ""
# while(len(key) != 4 and len(key) != 9):
#     key = input("Please input 4 or 9 integer key: ")
#     key = key.split(" ")



def generate_Matrix(key):
    size = int(math.sqrt(len(key)))
    lst = []
    temp_Lst = []
    for i in range(len(key)):
        temp_Lst.append(int(key[i]))
        if((i+1)%(size) == 0 and i!=0):
            lst.append(temp_Lst)
            temp_Lst = []
    return lst

def inverse_Matrix(matrix):
    det = 0
    if(len(matrix) == 2):
        det = (matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1])%26
        matrix[1][1],matrix[0][0] = matrix[0][0],matrix[1][1]
        matrix[0][1] = - matrix[0][1]
        matrix[1][0] = - matrix[1][0]
    elif(len(matrix) == 3):
        gfg = np.matrix(matrix)
        det = round(np.linalg.det(gfg),0)
        # applying matrix.getH() method
        try:
            matrix = np.linalg.inv(gfg)
            matrix = matrix.tolist()
        except:
            return []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = int(round((matrix[i][j]*det)%26,0))
    factor = int(extended_euclid(26,abs(det%26)))
    if(factor != 0):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = int(factor*matrix[i][j]%26)
        return matrix
    else:
        return []

def encryptTwoLetters(matrix,letter_lst):
    output_letter_lst = []
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix[i])):
            sum += matrix[i][j] * (ord(letter_lst[j].lower())-97)
        output_letter_lst.append(chr(sum%26+97))
    return "".join(output_letter_lst)

def encryptHillcipher(new_string,key):
    valid_letters = "abcdefghijklmnopqrstuvwxyz"
    new_string = new_string.lower()
    nonalphaChars = []
    plaintext = ""
    for i in range(len(new_string)):
        char = new_string[i]
        if char in valid_letters:
            plaintext += char
        else:
            nonalphaChars += [(i,char)] 
    matrix = generate_Matrix(key)
    encryption_size = len(matrix)
    while(len(plaintext)%encryption_size != 0):
        plaintext+="x"

    ciphertext = ""
    subStr = ""
    for i in range(len(plaintext)):
        subStr += plaintext[i]
        if((i+1)%encryption_size == 0):
            
            ciphertext += encryptTwoLetters(matrix,subStr)
            subStr = ""
    for i in range(len(nonalphaChars)):
        index = nonalphaChars[i][0]
        char = nonalphaChars[i][1]
        ciphertext  = ciphertext[:index] + char + ciphertext[index:]
    return ciphertext

def decryptHillcipher(new_string,key):
    matrix = generate_Matrix(key)
    matrix = inverse_Matrix(matrix)
    if(matrix == []):
        return "-1"

    valid_letters = "abcdefghijklmnopqrstuvwxyz"
    new_string = new_string.lower()
    nonalphaChars = []
    ciphertext = ""
    for i in range(len(new_string)):
        char = new_string[i]
        if char in valid_letters:
            ciphertext += char
        else:
            nonalphaChars += [(i,char)] 
    encryption_size = len(matrix)
    while(len(ciphertext)%encryption_size != 0):
        ciphertext+="x"

    plaintext = ""
    subStr = ""
    for i in range(len(ciphertext)):
        subStr += ciphertext[i]
        if((i+1)%encryption_size == 0):
            
            plaintext += encryptTwoLetters(matrix,subStr)
            subStr = ""
    if(plaintext[len(plaintext)-1] == 'x'):
        plaintext = plaintext[:len(plaintext)-1]
    for i in range(len(nonalphaChars)):
        index = nonalphaChars[i][0]
        char = nonalphaChars[i][1]
        plaintext  = plaintext[:index] + char + plaintext[index:]
    return plaintext

