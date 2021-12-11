# plaintext = input("Please Enter text: ").lower()
# key = input("Please Enter Key: ").lower()

def displayMatrix(lst):
    for line in lst:
        print(line)

def fixText(plaintext):
    i=0
    while(i<len(plaintext)-1):
        if(plaintext[i] == plaintext[i+1] and plaintext[i] != 'q'):
            plaintext = plaintext[:i+1]+'q'+plaintext[i+1:]
            i+=1
        elif(plaintext[i] == plaintext[i+1]):
            plaintext = plaintext[:i+1]+'z'+plaintext[i+1:]
            i+=1
        i+=1
    if(len(plaintext)%2 != 0 and plaintext[len(plaintext)-1] != 'x'):
        plaintext += 'x'
    elif(len(plaintext)%2 != 0):
        plaintext += 'q'
    return plaintext

def fixDecryptedText(plaintext):
    if(plaintext[len(plaintext)-1] == 'q' or plaintext[len(plaintext)-1] == 'x'):
        plaintext = plaintext[:len(plaintext)-1]
    i=0
    while(i<len(plaintext)-2):
        if(plaintext[i] == plaintext[i+2] and (plaintext[i+1] == 'q' or plaintext[i+1] == 'z')):
            plaintext = plaintext[:i+1]+plaintext[i+2:]
            i+=1
        i+=1
    return plaintext

def generateMatrix(key):
    remaining_alpha = "abcdefghiklmnopqrstuvwxyz"
    used_alpha = ""
    lst = []
    while(len(lst) < 5):
        lstRow = []
        while(len(lstRow) < 5):
            if(len(key) != 0):
                if(key[0] not in used_alpha):
                    if(key[0] == 'i' or key[0] == 'j'):
                        lstRow.append('i/j')
                        remaining_alpha = remaining_alpha.replace('i','')
                    else:
                        lstRow.append(key[0])
                        for i in range(len(remaining_alpha)-1):
                            if(remaining_alpha[i]==key[0]):
                                remaining_alpha = remaining_alpha.replace(key[0],"")
                    used_alpha += key[0]
            else:
                if(remaining_alpha[0] == 'i'):
                    lstRow.append('i/j')
                else:
                    lstRow.append(remaining_alpha[0])
                remaining_alpha = remaining_alpha[1:]
                
            key = key[1:]
        lst.append(lstRow)
    return lst


def encryptTwoLettersPlayfair(lst,string):
    alpha = "abcedfghijklmnopqrstuvwxyz"
    letter1 = string[0]
    letter2 = string[1]
    coordinates1 = [0,0]
    coordinates2 = [0,0]
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if letter1 in lst[i][j]:
                coordinates1 = [i,j]
            elif letter2 in lst[i][j]:
                coordinates2 = [i,j]
    if(coordinates1[1] != coordinates2[1] and coordinates1[0] != coordinates2[0]):
        coordinates2[1],coordinates1[1] = coordinates1[1],coordinates2[1]
    elif(coordinates1[0] == coordinates2[0]):
        coordinates1[1] = (coordinates1[1]+1)%5
        coordinates2[1] = (coordinates2[1]+1)%5
    elif(coordinates1[1] == coordinates2[1]):
        coordinates1[0] = (coordinates1[0]+1)%5
        coordinates2[0] = (coordinates2[0]+1)%5
    if(letter1 in alpha):
        letter1 = lst[coordinates1[0]][coordinates1[1]]
    if(letter2 in alpha):
        letter2 = lst[coordinates2[0]][coordinates2[1]]
    if(letter2 == "i/j"):
        letter2 = 'i'
    if(letter1 == "i/j"):
        letter1 = 'i'
    return letter1+letter2

def encrypt(plainText,key):
    lst = generateMatrix(key)

    ciphertext = ""
    subStr = ""
    for i in range(len(plainText)):
        subStr += plainText[i]
        if(i%2 != 0):
            ciphertext += encryptTwoLettersPlayfair(lst,subStr)
            subStr = ""
    # for i in range(len(nonalphaChars)):
    #     index = nonalphaChars[i][0]
    #     char = nonalphaChars[i][1]
    #     ciphertext  = ciphertext[:index] + char + ciphertext[index:]
    return ciphertext

def decryptTwoLettersPlayfair(lst,string):
    alpha = "abcedfgiklmnopqrstuvwxyz"
    letter1 = string[0]
    letter2 = string[1]
    coordinates1 = [0,0]
    coordinates2 = [0,0]
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if letter1 in lst[i][j]:
                coordinates1 = [i,j]
            elif letter2 in lst[i][j]:
                coordinates2 = [i,j]
    if(coordinates1[1] != coordinates2[1] and coordinates1[0] != coordinates2[0]):
        coordinates2[1],coordinates1[1] = coordinates1[1],coordinates2[1]
    elif(coordinates1[0] == coordinates2[0]):
        coordinates1[1] = (coordinates1[1]-1)%5
        coordinates2[1] = (coordinates2[1]-1)%5
    elif(coordinates1[1] == coordinates2[1]):
        coordinates1[0] = (coordinates1[0]-1)%5
        coordinates2[0] = (coordinates2[0]-1)%5
    if(letter1 in alpha):
        letter1 = lst[coordinates1[0]][coordinates1[1]]
    if(letter2 in alpha):
        letter2 = lst[coordinates2[0]][coordinates2[1]]
    return letter1+letter2

def decrypt(cipherText,key):
    lst = generateMatrix(key)
    plainText = ""
    subStr = ""
    for i in range(len(cipherText)):
        subStr += cipherText[i]
        if(i%2 != 0):
            plainText += decryptTwoLettersPlayfair(lst,subStr)
            subStr = ""
    plainText = fixDecryptedText(plainText)
    
    return plainText


def encryptPlayfair(plainText,key):
    valid_letters = "abcdefghijklmnopqrstuvwxyz"
    plainText = plainText.lower()
    nonalphaChars = []
    for i in range(len(plainText)):
        char = plainText[i]
        if char in valid_letters:
            print()
        else:
            nonalphaChars += [(i,char)] 
    plainText = plainText.replace("."," ")
    lst = plainText.split(" ")
    print(lst)
    for i in range(len(lst)):
        lst[i] = fixText(lst[i])
    # plainText = "".join(lst)
    # plainText = fixText(plainText)

    for i in range(len(lst)):
        lst[i] = encrypt(lst[i],key)
    return " ".join(lst)

def decryptPlayfair(ciphertext,key):
    valid_letters = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ciphertext.lower()
    nonalphaChars = []
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char in valid_letters:
            print()
        else:
            nonalphaChars += [(i,char)] 
    ciphertext = ciphertext.replace("."," ")
    lst = ciphertext.split(" ")
    # print(lst)
    for i in range(len(lst)):
        lst[i] = fixText(lst[i])


    for i in range(len(lst)):
        lst[i] = decrypt(lst[i],key)
    return " ".join(lst)


