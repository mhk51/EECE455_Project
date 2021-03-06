from extended_euclid import extended_euclid

# a = int(input("input a: "))
# b = int(input("input b: "))
# P = input("input plaintext: ")

def encryptaffinecipher(a, b ,P):
    output = ""
    for i in range(len(P)):
        if (ord(P[i])>= 97 and ord(P[i])<=122):
            output += chr((a*(ord(P[i])-97) + b)%26 + 97)
        elif (ord(P[i])>= 65 and ord(P[i])<=90):
            output += chr((a*(ord(P[i])-65) + b)%26 + 65)
        else:
            output += P[i]
    return output

def decryptaffinecipher(a, b, C):
    output = ""
    inverse_A = extended_euclid(26,a)
    if(inverse_A == 0):
        return "No Inverse"
    for i in range(len(C)):
        if (ord(C[i])>= 97 and ord(C[i])<=122):
            output += chr((inverse_A*((ord(C[i])-97)-b))%26 + 97)
        elif (ord(C[i])>= 65 and ord(C[i])<=90):
            output += chr((inverse_A*((ord(C[i])-65)-b))%26 + 65)
        else:
            output += C[i]
    return output

def crackaffinecipher(letter1,letter2):
    lst = [-1,-1]
    letter1 = letter1.lower()
    letter2 = letter2.lower()
    x = ord(letter1) - 97
    y = ord(letter2) - 97
    # x = (4a + b)%26
    # y = (19a + b)%26
    # first condition (y-x) = 15a%26
    a = 0 
    while (True):
        if ((y-x)%26 == (15*a)%26):
            break
        else:
            a = a + 1
    # second condition x = (4a + b)%26
    b = 0
    while (True):
        if (x%26 == (4*a + b)%26):
            break
        else:
            b = b + 1
    return "a ="+str(a)+"    b="+str(b)

def generatekey(string, key):
    output = key
    if (len(string) > len(key)):
        for i in range(len(string) - len(key)):
            output += key[i%len(key)]
    return output

def Encryptvigenere(string, key):
    output = ""
    for i in range(len(string)):
        if (ord(string[i])>= 97 and ord(string[i])<=122):
            if (ord(key[i])>= 97 and ord(key[i])<=122):
                output += chr((ord(string[i])-97 + ord(key[i])-97) % 26 + 97)
            else:
                output += chr((ord(string[i])-97 + ord(key[i])-65) % 26 + 97)
        elif (ord(string[i])>= 65 and ord(string[i])<=90):
            if (ord(key[i])>= 97 and ord(key[i])<=122):
                output += chr((ord(string[i])-65 + ord(key[i])-97) % 26 + 65)
            else:
                output += chr((ord(string[i])-65 + ord(key[i])-65) % 26 + 65)
        else:
            output += string[i]
    return output

def Decryptvigenere(string, key):
    output = ""
    for i in range(len(string)):
        if (ord(string[i])>= 97 and ord(string[i])<=122):
            if (ord(key[i])>= 97 and ord(key[i])<=122):
                output += chr((ord(string[i])-97 - (ord(key[i])-97)) % 26 + 97)
            else:
                output += chr((ord(string[i])-97 - (ord(key[i])-65)) % 26 + 97)
        elif (ord(string[i])>= 65 and ord(string[i])<=90):
            if (ord(key[i])>= 97 and ord(key[i])<=122):
                output += chr((ord(string[i])-65 - (ord(key[i])-97)) % 26 + 65)
            else:
                output += chr((ord(string[i])-65 - (ord(key[i])-65)) % 26 + 65)
        else:
            output += string[i]
    return output

# print(encryptaffinecipher(a,b,P))
# C = input("input ciphertext: ")
# print(decryptaffinecipher(a,b,C))
# x = input("input the most common letter: ")
# y = input("input the 2nd most common letter: ")
# print(crackaffinecipher(x,y))
# c = input("input string: ")
# d = input("input key: ")

# print(generatekey(c,d))
# print(Encryptvigenere(c,generatekey(c,d)))
# e = input("input cipher: ")
# print(generatekey(e,d))
# print(Decryptvigenere(e,generatekey(e,d)))
