from math import acos, ceil
from tkinter import *
import tkinter as tk
from tkinter import ttk
from numpy.core.fromnumeric import size

from numpy.matrixlib.defmatrix import matrix
from encyptions import encryptaffinecipher,Encryptvigenere,decryptaffinecipher,Decryptvigenere,crackaffinecipher,generatekey
from extended_euclid import extended_euclid
from monoalphabetic_cipher import encrypt_Monoalphabetic,decrypt_Monoalphabetic
from playfair import decryptPlayfair, encryptPlayfair,generateMatrix
from hill_cipher import encryptHillcipher,decryptHillcipher
root = Tk()
root.geometry('800x600')


    

tab_control = ttk.Notebook(root)

tab1 = Frame(tab_control)

tab2 = Frame(tab_control)

tab3 = Frame(tab_control)

tab4 = Frame(tab_control)

tab5 = Frame(tab_control)

tab6 = Frame(tab_control)

tab7 = Frame(tab_control)

tab8 = Frame(tab_control)


tab_control.add(tab2, text='Affine')
tab_control.add(tab5,text='Crack Affine')

tab_control.add(tab3, text='Vigenere')

tab_control.add(tab4,text = "Monoalphabetic")

tab_control.add(tab6,text = 'Playfair')

tab_control.add(tab7,text="Hill Cipher 2x2")

tab_control.add(tab8,text="Hill Cipher 3x3")

tab_control.add(tab1, text='Extended Euclid')


description_Extended_Euclid = Label(tab1,text="Use the extended Euclidean algorithm to find the multiplicative inverse of b mod m.\n\
Input the value of b in the “b” section.\n\
Input the value of m in the “m” section.")
description_Extended_Euclid.pack(side=TOP)

extended_euclid_Button = Button(tab1,height=3,width=15,text="Compute",command=lambda:compute_Extended_Euclid())
extended_euclid_Button.pack(side = TOP)
extended_euclid_Button.place(relx=.5,rely=.38,anchor=CENTER)
    
inputM = Entry(tab1,width=3)
inputM.pack(side = RIGHT)
inputM.place(relx=.45,rely=.5,anchor=CENTER)

label_CrackAffine_Letter1 = Label(tab1,text="m=")
label_CrackAffine_Letter1.pack(side = RIGHT)
label_CrackAffine_Letter1.place(relx=.37,rely=.5,anchor=CENTER)

inputB = Entry(tab1,width=3)
inputB.pack(side = RIGHT)
inputB.place(relx=.6,rely=.5,anchor=CENTER)

label_CrackAffine_Letter2 = Label(tab1,text="b=")
label_CrackAffine_Letter2.pack(side = RIGHT)
label_CrackAffine_Letter2.place(relx=.52,rely=.5,anchor=CENTER)


outputExtended_Euclid = Entry(tab1)
outputExtended_Euclid.pack(side = BOTTOM)
outputExtended_Euclid.place(relx=.5,rely=.6,anchor=CENTER)


def compute_Extended_Euclid():
    m = inputM.get()
    b = inputB.get()
    outputExtended_Euclid.delete(0,"end")
    outputExtended_Euclid.insert(0,extended_euclid(int(m),int(b)))

def encrypt_Affine():
    a = inputA_Affine.get()
    b = inputB_Affine.get()
    p = plaintext_Affine.get()
    plaintext_Affine.delete(0,"end")
    ciphertext_Affine.delete(0,"end")
    ciphertext_Affine.insert(0,encryptaffinecipher(int(a),int(b),p))
def decrypt_Affine():
    a = inputA_Affine.get()
    b = inputB_Affine.get()
    p = ciphertext_Affine.get()
    ciphertext_Affine.delete(0,"end")
    plaintext_Affine.delete(0,"end")
    plaintext_Affine.insert(0,decryptaffinecipher(int(a),int(b),p))

def crackAffine():
    letter1 = inputLetter1_CrackAffine.get("1.0","end-1c")
    letter2 = inputLetter2_CrackAffine.get("1.0","end-1c")
    output_CrackAffine.delete(0,"end")
    output_CrackAffine.insert(0,crackaffinecipher(letter1,letter2))

def encrypt_Vigenere():
    plaintext = plaintext_Vigenere.get()
    plaintext_Vigenere.delete(0,"end")
    key = key_Vigenere.get()
    key = generatekey(plaintext,key)
    cipherText_Vigenere.delete(0,"end")
    cipherText_Vigenere.insert(0,Encryptvigenere(plaintext,key))

def decrypt_Vigenere():
    ciphertext = cipherText_Vigenere.get()
    cipherText_Vigenere.delete(0,"end")
    key = key_Vigenere.get()
    key = generatekey(ciphertext,key)
    plaintext_Vigenere.delete(0,"end")
    plaintext_Vigenere.insert(0,Decryptvigenere(ciphertext,key))

def encrypt_Mono():
    plaintext = plaintext_Mono.get()
    key = key_Mono.get()
    plaintext_Mono.delete(0,"end")
    cipherText_Mono.delete(0,"end")
    cipherText_Mono.insert(0,encrypt_Monoalphabetic(plaintext,key))

def decrypt_Mono():
    plaintext = cipherText_Mono.get()
    key = key_Mono.get()
    cipherText_Mono.delete(0,"end")
    plaintext_Mono.delete(0,"end")
    plaintext_Mono.insert(0,decrypt_Monoalphabetic(plaintext,key))

def encrypt_Playfair():
    plaintext = plaintext_Playfair.get()
    key = key_Playfair.get()
    lst = generateMatrix(key)
    count = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            playfairMatrix_Lst[count]["text"] = lst[i][j]
            count+=1
    plaintext_Playfair.delete(0,"end")
    cipherText_Playfair.delete(0,"end")
    cipherText_Playfair.insert(0,encryptPlayfair(plaintext,key))

def decrypt_Playfair():
    plaintext = cipherText_Playfair.get()
    key = key_Playfair.get()
    lst = generateMatrix(key)
    count = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            playfairMatrix_Lst[count]["text"] = lst[i][j]
            count+=1
    cipherText_Playfair.delete(0,"end")
    plaintext_Playfair.delete(0,"end")
    plaintext_Playfair.insert(0,decryptPlayfair(plaintext,key))

def encrypt_Hill():
    plaintext = plaintext_Hill.get()
    key = []
    plaintext_Hill.delete(0,"end")
    for i in range(len(matrix_Text_Hill)):
        key.append(matrix_Text_Hill[i].get())
    if(len(key) != 4 and len(key) != 9):
        cipherText_Hill.delete(0,"end")
        cipherText_Hill.insert(0,"Invalid Key")
        return
    cipherText_Hill.delete(0,"end")
    cipherText_Hill.insert(0,encryptHillcipher(plaintext,key))

def decrypt_Hill():
    ciphertext = cipherText_Hill.get()
    key = []
    for i in range(len(matrix_Text_Hill)):
        key.append(matrix_Text_Hill[i].get())
    if(len(key) != 4 and len(key) != 9):
        plaintext_Hill.delete(0,"end")
        plaintext_Hill.insert(0,"Invalid Key")
        return
    plaintext_Hill.delete(0,"end")
    string = decryptHillcipher(ciphertext,key)
    if(string == "-1"):
        plaintext_Hill.insert(0,"No inverse")
    else:
        plaintext_Hill.insert(0,string)
        cipherText_Hill.delete(0,"end")

def encrypt_Hill_3x3():
    plaintext = plaintext_Hill_3x3.get()
    key = []
    for i in range(len(matrix_Text_Hill_3x3)):
        key.append(matrix_Text_Hill_3x3[i].get())
    if(len(key) != 4 and len(key) != 9):
        cipherText_Hill_3x3.delete(0,"end")
        cipherText_Hill_3x3.insert(0,"Invalid Key")
        return
    cipherText_Hill_3x3.delete(0,"end")
    cipherText_Hill_3x3.insert(0,encryptHillcipher(plaintext,key))

def decrypt_Hill_3x3():
    ciphertext = cipherText_Hill_3x3.get()
    key = []
    for i in range(len(matrix_Text_Hill_3x3)):
        key.append(matrix_Text_Hill_3x3[i].get())
    if(len(key) != 4 and len(key) != 9):
        plaintext_Hill_3x3.delete(0,"end")
        plaintext_Hill_3x3.insert(0,"Invalid Key")
        return
    plaintext_Hill_3x3.delete(0,"end")
    string = decryptHillcipher(ciphertext,key)
    if(string == "-1"):
        plaintext_Hill_3x3.insert(0,"No inverse")
    else:
        plaintext_Hill_3x3.insert(0,string)
        cipherText_Hill_3x3.delete(0,"end")

tab7.columnconfigure(0, weight=1)
tab7.rowconfigure(0, weight=1)

playfairMatrix = Frame(tab6, bg="Gray")
playfairMatrix.grid(sticky=(N,E,S,W))
playfairMatrix.columnconfigure(0, weight=1)


F1 = Frame(playfairMatrix, bg="Green", bd=2, relief=GROOVE)
F1.grid(row=1, column=0, sticky=(N,W))


Can1 = Canvas(playfairMatrix, bg="Yellow")
Can1.grid(row=3, column=0, sticky=(N,W))

playfairMatrix_Lst = []

F2 = Frame(Can1, bg="Blue", bd=2, relief=GROOVE)
F2.grid(row=0, column=0, sticky=(N,W))
rows = 5
for i in range(0,rows):
    for j in range(0,5):
        button = Button(F2,height=4,width=8,text="")
        button.grid(row=i, column=j, sticky='news')
        playfairMatrix_Lst.append(button)



F3 = Frame(playfairMatrix, bg="Red", bd=2, relief=GROOVE)
F3.grid(row=5, column=0, sticky=(N,W))

playfairMatrix.pack(side = LEFT)




tab7.columnconfigure(0, weight=1)
tab7.rowconfigure(0, weight=1)

FMas = Frame(tab7, bg="Gray")
FMas.grid(sticky=(N,E,S,W))
FMas.columnconfigure(0, weight=1)


F1 = Frame(FMas, bg="Green", bd=2, relief=GROOVE)
F1.grid(row=1, column=0, sticky=(N,W))


Can1 = Canvas(FMas, bg="Yellow")
Can1.grid(row=3, column=0, sticky=(N,W))

large_font = ('Verdana',30)

F2 = Frame(Can1, bg="Blue", bd=2, relief=GROOVE)
F2.grid(row=0, column=0, sticky=(N,W))
matrix_Text_Hill = []
rows = 2
for i in range(0,rows):
    for j in range(0,2):
        button = Entry(F2,width=2,font=large_font)
        button.grid(row=i, column=j, sticky='news')
        matrix_Text_Hill.append(button)


F3 = Frame(FMas, bg="Red", bd=2, relief=GROOVE)
F3.grid(row=5, column=0, sticky=(N,W))

FMas.pack(side = LEFT)


tab8.columnconfigure(0, weight=1)
tab8.rowconfigure(0, weight=1)

FMas = Frame(tab8, bg="Gray")
FMas.grid(sticky=(N,E,S,W))
FMas.columnconfigure(0, weight=1)


F1 = Frame(FMas, bg="Green", bd=2, relief=GROOVE)
F1.grid(row=1, column=0, sticky=(N,W))


Can1 = Canvas(FMas, bg="Yellow")
Can1.grid(row=3, column=0, sticky=(N,W))

large_font = ('Verdana',30)

F2 = Frame(Can1, bg="Blue", bd=2, relief=GROOVE)
F2.grid(row=0, column=0, sticky=(N,W))
matrix_Text_Hill_3x3 = []
rows = 3
for i in range(0,rows):
    for j in range(0,3):
        button = Entry(F2,width=2,font=large_font)
        button.grid(row=i, column=j, sticky='news')
        matrix_Text_Hill_3x3.append(button)


F3 = Frame(FMas, bg="Red", bd=2, relief=GROOVE)
F3.grid(row=5, column=0, sticky=(N,W))

FMas.pack(side = LEFT)


description_Affine = Label(tab2,text="A generalization of the Caesar Cipher is the Affine Cipher given by: C = (a.P + b) mod 26,\n Where P is the plain character and C is the cipher character, a and b are coefficients.\n The decryption of the Affine Cipher is given by: P = a-1 (C – b) mod 26, where a-1 is the inverse of a mod 26.\n Note that characters are assigned values of A=0 and Z=25.\n\
Input the word or sentence you want to encrypt in the “plaintext” section.\n\
Input the word or sentence you want to decrypt in the “ciphertext” section.\n\
Input the values of the coefficients a and b in the “a” and “b” sections.")
description_Affine.pack(side = TOP)
encrypt_Affine_Button = Button(tab2,width=10,height=2,text="Encrypt",command=lambda:encrypt_Affine())
encrypt_Affine_Button.pack(side = TOP)
encrypt_Affine_Button.place(relx=.4,rely=.3,anchor=CENTER)
decrypt_Affine_Button = Button(tab2,width=10,height=2,text="Decrypt",command=lambda:decrypt_Affine())
decrypt_Affine_Button.pack(side = TOP)
decrypt_Affine_Button.place(relx=.6,rely=.3,anchor=CENTER)
    
inputA_Affine = Entry(tab2,width=3)
inputA_Affine.pack(side = RIGHT)
inputA_Affine.place(relx=.45,rely=.6,anchor=CENTER)

label_A_Affine = Label(tab2,text="a=")
label_A_Affine.pack(side = RIGHT)
label_A_Affine.place(relx=.42,rely=.6,anchor=CENTER)


inputB_Affine = Entry(tab2,width=3)
inputB_Affine.pack(side = RIGHT)
inputB_Affine.place(relx=.55,rely=.6,anchor=CENTER)

label_B_Affine = Label(tab2,text="b=")
label_B_Affine.pack(side = RIGHT)
label_B_Affine.place(relx=.52,rely=.6,anchor=CENTER)

plaintext_Affine = Entry(tab2,width=20)
plaintext_Affine.pack(side = RIGHT)
plaintext_Affine.place(relx=.4,rely=.5,anchor=CENTER)

label_Affine_Plaintext = Label(tab2,text="PlainText:")
label_Affine_Plaintext.pack(side = RIGHT)
label_Affine_Plaintext.place(relx=.4,rely=.45,anchor=CENTER)

ciphertext_Affine = Entry(tab2,width=20)
ciphertext_Affine.pack(side = RIGHT)
ciphertext_Affine.place(relx=.6,rely=.5,anchor=CENTER)

label_Affine_ciphertext = Label(tab2,text="CipherText:")
label_Affine_ciphertext.pack(side = RIGHT)
label_Affine_ciphertext.place(relx=.6,rely=.45,anchor=CENTER)




description_CrackAffine = Label(tab5,text = "We know that the most frequent letters of the English alphabet are E and T.\n After doing Affine encryption to a plaintext, the most frequent letters became \"First Letter\" and \"Second Letter\".\n The values of a and b are:")
description_CrackAffine.pack(side =TOP)
encrypt_CrackAffine_Button = Button(tab5,height=3,width=15,text="Crack",command=lambda:crackAffine())
encrypt_CrackAffine_Button.pack(side = TOP)
encrypt_CrackAffine_Button.place(relx=.5,rely=.38,anchor=CENTER)
    
inputLetter1_CrackAffine = Text(tab5,height=1,width=3)
inputLetter1_CrackAffine.pack(side = RIGHT)
inputLetter1_CrackAffine.place(relx=.45,rely=.5,anchor=CENTER)

label_CrackAffine_Letter1 = Label(tab5,text="First Letter:")
label_CrackAffine_Letter1.pack(side = RIGHT)
label_CrackAffine_Letter1.place(relx=.37,rely=.5,anchor=CENTER)

inputLetter2_CrackAffine = Text(tab5,height=1,width=3)
inputLetter2_CrackAffine.pack(side = RIGHT)
inputLetter2_CrackAffine.place(relx=.6,rely=.5,anchor=CENTER)

label_CrackAffine_Letter2 = Label(tab5,text="Second Letter:")
label_CrackAffine_Letter2.pack(side = RIGHT)
label_CrackAffine_Letter2.place(relx=.52,rely=.5,anchor=CENTER)


output_CrackAffine = Entry(tab5)
output_CrackAffine.pack(side = BOTTOM)
output_CrackAffine.place(relx=.5,rely=.6,anchor=CENTER)





description_Vigenere = Label(tab3,text = "Use the Vigenere cipher to encrypt/decrypt a word or a sentence using a special key.\n\
Input the word or sentence you want to encrypt in the “plaintext” section.\n\
Input the word or sentence you want to decrypt in the “ciphertext” section.\n\
Input the values of the key in the “key” section.")
description_Vigenere.pack(side =TOP)

encrypt_Vigenere_Button = Button(tab3,height=2,width=10,text = "Encrypt",command = lambda:encrypt_Vigenere())
encrypt_Vigenere_Button.pack(side = TOP)
encrypt_Vigenere_Button.place(relx=.4,rely=.3,anchor=CENTER)
decrypt_Vigenere_Button = Button(tab3,height=2,width=10,text = "Decrypt",command=lambda:decrypt_Vigenere())
decrypt_Vigenere_Button.pack(side = TOP)
decrypt_Vigenere_Button.place(relx=.6,rely=.3,anchor=CENTER)


plaintext_Vigenere = Entry(tab3,width=30)
plaintext_Vigenere.pack(side = RIGHT)
plaintext_Vigenere.place(relx =.35,rely=.5,anchor=CENTER)

label_Vigenere_Plaintext = Label(tab3,text="PlainText:")
label_Vigenere_Plaintext.pack(side = RIGHT)
label_Vigenere_Plaintext.place(relx=.35,rely=.45,anchor=CENTER)

key_Vigenere = Entry(tab3,width=20)
key_Vigenere.pack(side = RIGHT)
key_Vigenere.place(relx=.5, rely=.7,anchor= CENTER)

label_Vigenere_Key = Label(tab3,text="Key:")
label_Vigenere_Key.pack(side = RIGHT)
label_Vigenere_Key.place(relx=.4,rely=.7,anchor=CENTER)


cipherText_Vigenere = Entry(tab3,width=30)
cipherText_Vigenere.pack(side = BOTTOM)
cipherText_Vigenere.place(relx=.65,rely=.5,anchor=CENTER)

label_Vigenere_Ciphertext = Label(tab3,text="Ciphertext:")
label_Vigenere_Ciphertext.pack(side = BOTTOM)
label_Vigenere_Ciphertext.place(relx=.65,rely=.45,anchor=CENTER)




description_Mono = Label(tab4,text="Input the word or sentence you want to encrypt in the “plaintext” section.\n\
Input the word or sentence you want to decrypt in the “ciphertext” section.\n\
Input the values of the key in the “key” section.")
description_Mono.pack(side=TOP)

encrypt_Mono_Button = Button(tab4,height=2,width=10,text = "Encrypt",command = lambda:encrypt_Mono())
encrypt_Mono_Button.pack(side = TOP)
encrypt_Mono_Button.place(relx=.4,rely=.3,anchor=CENTER)
decrypt_Mono_Button = Button(tab4,height=2,width=10,text = "Decrypt",command=lambda:decrypt_Mono())
decrypt_Mono_Button.pack(side = TOP)
decrypt_Mono_Button.place(relx=.6,rely=.3,anchor=CENTER)


plaintext_Mono = Entry(tab4,width=30)
plaintext_Mono.pack(side = RIGHT)
plaintext_Mono.place(relx =.35,rely=.5,anchor=CENTER)

label_Mono_Plaintext = Label(tab4,text="PlainText:")
label_Mono_Plaintext.pack(side = RIGHT)
label_Mono_Plaintext.place(relx=.35,rely=.45,anchor=CENTER)

key_Mono = Entry(tab4,width=20)
key_Mono.pack(side = RIGHT)
key_Mono.place(relx=.5, rely=.7,anchor= CENTER)

label_Mono_Key = Label(tab4,text="Key:")
label_Mono_Key.pack(side = RIGHT)
label_Mono_Key.place(relx=.4,rely=.7,anchor=CENTER)


cipherText_Mono = Entry(tab4,width=30)
cipherText_Mono.pack(side = BOTTOM)
cipherText_Mono.place(relx=.65,rely=.5,anchor=CENTER)

label_Mono_Ciphertext = Label(tab4,text="Ciphertext:")
label_Mono_Ciphertext.pack(side = BOTTOM)
label_Mono_Ciphertext.place(relx=.65,rely=.45,anchor=CENTER)


description_Playfair = Label(tab6,text="Use the Playfair code to encrypt/decrypt a word or a sentence using a special key.\n\
Input the word or sentence you want to encrypt in the “plaintext” section.\n\
Input the word or sentence you want to decrypt in the “ciphertext” section.\n\
Input the values of the key in the “key” section.")

description_Playfair.pack(side=TOP)


encrypt_Playfair_Button = Button(tab6,height=2,width=10,text = "Encrypt",command = lambda:encrypt_Playfair())
encrypt_Playfair_Button.pack(side = TOP)
encrypt_Playfair_Button.place(relx=.6,rely=.3,anchor=CENTER)
decrypt_Playfair_Button = Button(tab6,height=2,width=10,text = "Decrypt",command=lambda:decrypt_Playfair())
decrypt_Playfair_Button.pack(side = TOP)
decrypt_Playfair_Button.place(relx=.8,rely=.3,anchor=CENTER)


plaintext_Playfair = Entry(tab6,width=30)
plaintext_Playfair.pack(side = RIGHT)
plaintext_Playfair.place(relx =.55,rely=.5,anchor=CENTER)

label_Playfair_Plaintext = Label(tab6,text="PlainText:")
label_Playfair_Plaintext.pack(side = RIGHT)
label_Playfair_Plaintext.place(relx=.55,rely=.45,anchor=CENTER)

key_Playfair = Entry(tab6,width=20)
key_Playfair.pack(side = RIGHT)
key_Playfair.place(relx=.7, rely=.7,anchor= CENTER)

label_Playfair_Key = Label(tab6,text="Key:")
label_Playfair_Key.pack(side = RIGHT)
label_Playfair_Key.place(relx=.6,rely=.7,anchor=CENTER)


cipherText_Playfair = Entry(tab6,width=30)
cipherText_Playfair.pack(side = BOTTOM)
cipherText_Playfair.place(relx=.85,rely=.5,anchor=CENTER)

label_Playfair_Ciphertext = Label(tab6,text="Ciphertext:")
label_Playfair_Ciphertext.pack(side = BOTTOM)
label_Playfair_Ciphertext.place(relx=.85,rely=.45,anchor=CENTER)


description_Hill = Label(tab7,text="Fill the matrix given that will represent the key used in Hill cipher.\n\
Input the word or sentence you want to encrypt in the “plaintext” section.\n\
Input the word or sentence you want to decrypt in the “ciphertext” section.")

description_Hill.pack(side=TOP)


encrypt_Hill_Button = Button(tab7,height=2,width=10,text = "Encrypt",command = lambda:encrypt_Hill())
encrypt_Hill_Button.pack(side = TOP)
encrypt_Hill_Button.place(relx=.4,rely=.3,anchor=CENTER)
decrypt_Hill_Button = Button(tab7,height=2,width=10,text = "Decrypt",command=lambda:decrypt_Hill())
decrypt_Hill_Button.pack(side = TOP)
decrypt_Hill_Button.place(relx=.6,rely=.3,anchor=CENTER)


plaintext_Hill = Entry(tab7,width=30)
plaintext_Hill.pack(side = RIGHT)
plaintext_Hill.place(relx =.35,rely=.5,anchor=CENTER)

label_Hill_Plaintext = Label(tab7,text="PlainText:")
label_Hill_Plaintext.pack(side = RIGHT)
label_Hill_Plaintext.place(relx=.35,rely=.45,anchor=CENTER)

cipherText_Hill = Entry(tab7,width=30)
cipherText_Hill.pack(side = BOTTOM)
cipherText_Hill.place(relx=.65,rely=.5,anchor=CENTER)

label_Hill_Ciphertext = Label(tab7,text="Ciphertext:")
label_Hill_Ciphertext.pack(side = BOTTOM)
label_Hill_Ciphertext.place(relx=.65,rely=.45,anchor=CENTER)


description_Hill = Label(tab8,text="Fill the matrix given that will represent the key used in Hill cipher.\n\
Input the word or sentence you want to encrypt in the “plaintext” section.\n\
Input the word or sentence you want to decrypt in the “ciphertext” section.")

description_Hill.pack(side=TOP)

encrypt_Hill_3x3_Button = Button(tab8,height=2,width=10,text = "Encrypt",command = lambda:encrypt_Hill_3x3())
encrypt_Hill_3x3_Button.pack(side = TOP)
encrypt_Hill_3x3_Button.place(relx=.4,rely=.3,anchor=CENTER)
decrypt_Hill_3x3_Button = Button(tab8,height=2,width=10,text = "Decrypt",command=lambda:decrypt_Hill_3x3())
decrypt_Hill_3x3_Button.pack(side = TOP)
decrypt_Hill_3x3_Button.place(relx=.6,rely=.3,anchor=CENTER)


plaintext_Hill_3x3 = Entry(tab8,width=30)
plaintext_Hill_3x3.pack(side = RIGHT)
plaintext_Hill_3x3.place(relx =.35,rely=.5,anchor=CENTER)

label_Hill_3x3_Plaintext = Label(tab8,text="PlainText:")
label_Hill_3x3_Plaintext.pack(side = RIGHT)
label_Hill_3x3_Plaintext.place(relx=.35,rely=.45,anchor=CENTER)

cipherText_Hill_3x3 = Entry(tab8,width=30)
cipherText_Hill_3x3.pack(side = BOTTOM)
cipherText_Hill_3x3.place(relx=.65,rely=.5,anchor=CENTER)

label_Hill_3x3_Ciphertext = Label(tab8,text="Ciphertext:")
label_Hill_3x3_Ciphertext.pack(side = BOTTOM)
label_Hill_3x3_Ciphertext.place(relx=.65,rely=.45,anchor=CENTER)


tab_control.pack(expand=1, fill='both')

root.mainloop()