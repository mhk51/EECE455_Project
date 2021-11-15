a = int(input("input a: "))
b = int(input("input b: "))
P = input("input plaintext: ")

def encryptaffinecipher(a, b ,P):
    output = ""
    for i in range(len(P)):
        output += chr((a*(ord(P[i])-97) + b)%26 + 97)
    return output

# def decryptaffinecipher(a, b, C)
#     output = ""
#     for i in range(len(C)):
#         output += chr(ExtendedEuclideAlgorithm(a)*((ord(C[i]-97)-b))%26 + 97)


print(encryptaffinecipher(a,b,P))
