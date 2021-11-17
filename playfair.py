plaintext = input("Please Enter text: ").lower()
key = input("Please Enter Key: ").lower()

def fixText(plaintext):
    i=0
    while(i<len(plaintext)-1):
        if(plaintext[i] == plaintext[i+1] and plaintext[i] != 'x'):
            plaintext = plaintext[:i+1]+'x'+plaintext[i+1:]
            i+=1
        elif(plaintext[i] == plaintext[i+1]):
            plaintext = plaintext[:i+1]+'q'+plaintext[i+1:]
            i+=1
        i+=1
    if(len(plaintext)%2 != 0 and plaintext[len(plaintext)-1] != 'x'):
        plaintext += 'x'
    elif(len(plaintext)%2 != 0):
        plaintext += 'q'
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


print(fixText(plaintext))
lst = generateMatrix(key)

for i in range(5):
    print(lst[i])

