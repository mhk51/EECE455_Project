import math
from extended_euclid import extended_euclid
import numpy as np

plaintext = input("Please input text: ")

key = ""
while(len(key) != 4 and len(key) != 9):
    key = input("Please input 4 or 9 integer key: ")
    key = key.split(" ")



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
    A = np.array(matrix)
    det = int(round(np.linalg.det(A),0))
    factor = extended_euclid(26,abs(det))
    if(factor != 0):
        for i in range(len(A)):
            for j in range(len(A[i])):
                A[i] = factor*A[i]
        return A
    else:
        return -1

def encryptTwoLetters(matrix,letter_lst):
    output_letter_lst = []
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix[i])):
            sum += matrix[i][j] * (ord(letter_lst[j].lower())-97)
        output_letter_lst.append(chr(sum%26+97))
    return "".join(output_letter_lst)

def encryptHillcipher(plaintext,key):
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
    return ciphertext

def decryptHillcipher(ciphertext,key):
    matrix = generate_Matrix(key)
    matrix = inverse_Matrix(matrix)
    encryption_size = len(matrix)
    while(len(ciphertext)%encryption_size != 0):
        ciphertext+="x"

    ciphertext = ""
    subStr = ""
    for i in range(len(ciphertext)):
        subStr += ciphertext[i]
        if((i+1)%encryption_size == 0):
            
            ciphertext += encryptTwoLetters(matrix,subStr)
            subStr = ""
    return ciphertext

encryptHillcipher(plaintext,key)
    

inverse_Matrix(generate_Matrix(key))