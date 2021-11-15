from extended_euclid import extended_euclid

a = int(input("input a: "))
b = int(input("input b: "))
P = input("input plaintext: ")

def encryptaffinecipher(a, b ,P):
    output = ""
    for i in range(len(P)):
        output += chr((a*(ord(P[i])-97) + b)%26 + 97)
    return output

def decryptaffinecipher(a, b, C):
    output = ""
    if (extended_euclid(26,a) == 0):
        output = "No inverse for a, so we cannot decrypt!"
    else:
        for i in range(len(C)):
            output += chr((extended_euclid(26,a)*((ord(C[i])-97)-b))%26 + 97)
    return output


print(encryptaffinecipher(a,b,P))
C = input("input ciphertext: ")
print(decryptaffinecipher(a,b,C))
