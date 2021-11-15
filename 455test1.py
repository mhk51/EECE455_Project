from extended_euclid import extended_euclid

a = int(input("input a: "))
b = int(input("input b: "))
P = input("input plaintext: ")

# def extended_euclid(m,b):
#     A = [1,0,m]
#     B = [0,1,b]
#     print(A,B)
#     while(not(B[2] == 1) and not ( B[2] == 0)):
#         T = B
#         Q = A[2]//B[2]
#         B = [A[0]-Q*B[0],A[1]-Q*B[1],A[2]-Q*B[2]]
#         A = T
#         print(A,B)
#     if(B[2] == 0):
#         print("No inverse")
#     elif(B[2] == 1):
#         return B[1]+m

def encryptaffinecipher(a, b ,P):
    output = ""
    for i in range(len(P)):
        output += chr((a*(ord(P[i])-97) + b)%26 + 97)
    return output

def decryptaffinecipher(a, b, C):
    output = ""
    inverse_A = extended_euclid(26,a)
    if(inverse_A == 0):
        print("No Inverse")
        return
    for i in range(len(C)):
        output += chr((inverse_A*((ord(C[i])-97)-b))%26 + 97)
    return output


print(encryptaffinecipher(a,b,P))
C = input("input ciphertext: ")
print(decryptaffinecipher(a,b,C))
