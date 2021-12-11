from tkinter import *
import tkinter as tk
from tkinter import ttk
from numpy.core.fromnumeric import size

from numpy.matrixlib.defmatrix import matrix
from encyptions import encryptaffinecipher,Encryptvigenere,decryptaffinecipher,Decryptvigenere,crackaffinecipher
from extended_euclid import extended_euclid
from monoalphabetic_cipher import encrypt_Monoalphabetic,decrypt_Monoalphabetic
from playfair import decryptPlayfair, encryptPlayfair,generateMatrix
from hill_cipher import encryptHillcipher,decryptHillcipher
root = Tk()
root.geometry('800x600')


def retrieve_input():
    m = inputM.get("1.0","end-1c")
    b = inputB.get("1.0","end-1c")
    outputText.delete(0,"end")
    outputText.insert(0,extended_euclid(int(m),int(b)))
    

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

inputB = Text(tab1,height=1,width=3)
inputB.pack(side = RIGHT)

label1 = Label(tab1,text="b=")
label1.pack(side = RIGHT)

inputM = Text(tab1,height=1,width=3)
inputM.pack(side = RIGHT)

label2 = Label(tab1,text="m=")
label2.pack(side = RIGHT)

outputText = Entry(tab1)
outputText.pack(side = BOTTOM)


button = Button(tab1,text="Compute",command=lambda:retrieve_input())
button.pack(side = LEFT)


def encrypt_Affine():
    a = inputA_Affine.get("1.0","end-1c")
    b = inputB_Affine.get("1.0","end-1c")
    p = inputPlainText_Affine.get("1.0","end-1c")
    output_Affine.delete(0,"end")
    output_Affine.insert(0,encryptaffinecipher(int(a),int(b),p))
def decrypt_Affine():
    a = inputA_Affine.get("1.0","end-1c")
    b = inputB_Affine.get("1.0","end-1c")
    p = inputPlainText_Affine.get("1.0","end-1c")
    output_Affine.delete(0,"end")
    output_Affine.insert(0,decryptaffinecipher(int(a),int(b),p))

def crackAffine():
    letter1 = inputLetter1_CrackAffine.get("1.0","end-1c")
    letter2 = inputLetter2_CrackAffine.get("1.0","end-1c")
    output_CrackAffine.delete(0,"end")
    output_CrackAffine.insert(0,crackaffinecipher(letter1,letter2))

def encrypt_Vigenere():
    plaintext = inputString_Vigenere.get("1.0","end-1c")
    key = inputKey_Vigenere.get("1.0","end-1c")
    output_Vigenere.delete(0,"end")
    output_Vigenere.insert(0,Encryptvigenere(plaintext,key))

def decrypt_Vigenere():
    a = inputA_Affine.get("1.0","end-1c")
    b = inputB_Affine.get("1.0","end-1c")
    p = inputPlainText_Affine.get("1.0","end-1c")
    output_Vigenere.delete(0,"end")
    output_Vigenere.insert(0,decryptaffinecipher(int(a),int(b),p))

def encrypt_Mono():
    plaintext = inputString_Mono.get("1.0","end-1c")
    key = inputKey_Mono.get("1.0","end-1c")
    output_Mono.delete(0,"end")
    output_Mono.insert(0,encrypt_Monoalphabetic(plaintext,key))

def decrypt_Mono():
    plaintext = inputString_Mono.get("1.0","end-1c")
    key = inputKey_Mono.get("1.0","end-1c")
    output_Mono.delete(0,"end")
    output_Mono.insert(0,decrypt_Monoalphabetic(plaintext,key))

def encrypt_Playfair():
    plaintext = inputString_Playfair.get("1.0","end-1c")
    key = inputKey_Playfair.get("1.0","end-1c")
    lst = generateMatrix(key)
    count = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            playfairMatrix_Lst[count]["text"] = lst[i][j]
            count+=1
    output_Playfair.delete(0,"end")
    output_Playfair.insert(0,encryptPlayfair(plaintext,key))

def decrypt_Playfair():
    plaintext = inputString_Playfair.get("1.0","end-1c")
    key = inputKey_Playfair.get("1.0","end-1c")
    output_Playfair.delete(0,"end")
    output_Playfair.insert(0,decryptPlayfair(plaintext,key))

def encrypt_Hill():
    plaintext = inputString_Hill.get("1.0","end-1c")
    key = []
    for i in range(len(matrix_Text_Hill)):
        key.append(matrix_Text_Hill[i].get())
    if(len(key) != 4 and len(key) != 9):
        output_Hill.delete(0,"end")
        output_Hill.insert(0,"Invalid Key")
        return
    output_Hill.delete(0,"end")
    output_Hill.insert(0,encryptHillcipher(plaintext,key))

def decrypt_Hill():
    plaintext = inputString_Hill.get("1.0","end-1c")
    key = []
    for i in range(len(matrix_Text_Hill)):
        key.append(matrix_Text_Hill[i].get())
    if(len(key) != 4 and len(key) != 9):
        output_Hill.delete(0,"end")
        output_Hill.insert(0,"Invalid Key")
        return
    output_Hill.delete(0,"end")
    string = decryptHillcipher(plaintext,key)
    if(string == "-1"):
        output_Hill.insert(0,"No inverse")
    else:
        output_Hill.insert(0,string)

def encrypt_Hill_3x3():
    plaintext = inputString_Hill_3x3.get("1.0","end-1c")
    key = []
    for i in range(len(matrix_Text_Hill_3x3)):
        key.append(matrix_Text_Hill_3x3[i].get())
    if(len(key) != 4 and len(key) != 9):
        output_Hill_3x3.delete(0,"end")
        output_Hill_3x3.insert(0,"Invalid Key")
        return
    output_Hill_3x3.delete(0,"end")
    output_Hill_3x3.insert(0,encryptHillcipher(plaintext,key))

def decrypt_Hill_3x3():
    plaintext = inputString_Hill_3x3.get("1.0","end-1c")
    key = []
    for i in range(len(matrix_Text_Hill_3x3)):
        key.append(matrix_Text_Hill_3x3[i].get())
    if(len(key) != 4 and len(key) != 9):
        output_Hill_3x3.delete(0,"end")
        output_Hill_3x3.insert(0,"Invalid Key")
        return
    output_Hill_3x3.delete(0,"end")
    string = decryptHillcipher(plaintext,key)
    if(string == "-1"):
        output_Hill_3x3.insert(0,"No inverse")
    else:
        output_Hill_3x3.insert(0,string)

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



encrypt_Affine_Button = Button(tab2,text="Encrypt",command=lambda:encrypt_Affine())
encrypt_Affine_Button.pack(side = TOP)
decrypt_Affine_Button = Button(tab2,text="Decrypt",command=lambda:decrypt_Affine())
decrypt_Affine_Button.pack(side = TOP)
    
inputA_Affine = Text(tab2,height=1,width=3)
inputA_Affine.pack(side = RIGHT)

label1 = Label(tab2,text="a=")
label1.pack(side = RIGHT)

inputB_Affine = Text(tab2,height=1,width=3)
inputB_Affine.pack(side = RIGHT)

label2 = Label(tab2,text="b=")
label2.pack(side = RIGHT)

inputPlainText_Affine = Text(tab2,height=1,width=10)
inputPlainText_Affine.pack(side = RIGHT)

label3 = Label(tab2,text="PlainText:")
label3.pack(side = RIGHT)

output_Affine = Entry(tab2)
output_Affine.pack(side = BOTTOM)

outputLabel = Label(tab2,text="Output")
outputLabel.pack(side = BOTTOM)



encrypt_CrackAffine_Button = Button(tab5,text="Crack",command=lambda:crackAffine())
encrypt_CrackAffine_Button.pack(side = TOP)
    
inputLetter1_CrackAffine = Text(tab5,height=1,width=3)
inputLetter1_CrackAffine.pack(side = RIGHT)

label1 = Label(tab5,text="First Letter:")
label1.pack(side = RIGHT)

inputLetter2_CrackAffine = Text(tab5,height=1,width=3)
inputLetter2_CrackAffine.pack(side = RIGHT)

label2 = Label(tab5,text="Second Letter:")
label2.pack(side = RIGHT)


output_CrackAffine = Entry(tab5)
output_CrackAffine.pack(side = BOTTOM)

outputLabel = Label(tab5,text="Output")
outputLabel.pack(side = BOTTOM)





encrypt_Vigenere_Button = Button(tab3,text = "Encrypt",command = lambda:encrypt_Vigenere())
encrypt_Vigenere_Button.pack(side = TOP)
decrypt_Vigenere_Button = Button(tab3,text = "Decrypt",command=lambda:decrypt_Vigenere())
decrypt_Vigenere_Button.pack(side = TOP)


inputString_Vigenere = Text(tab3,height=1,width=10)
inputString_Vigenere.pack(side = RIGHT)

label1 = Label(tab3,text="PlainText:")
label1.pack(side = RIGHT)

inputKey_Vigenere = Text(tab3,height=1,width=10)
inputKey_Vigenere.pack(side = RIGHT)

label2 = Label(tab3,text="Key:")
label2.pack(side = RIGHT)


output_Vigenere = Entry(tab3)
output_Vigenere.pack(side = BOTTOM)

output_Vigenere_Label = Label(tab3,text="Output:")
output_Vigenere_Label.pack(side = BOTTOM)




encrypt_Mono_Button = Button(tab4,text = "Encrypt",command = lambda:encrypt_Mono())
encrypt_Mono_Button.pack(side = TOP)
decrypt_Mono_Button = Button(tab4,text = "Decrypt",command=lambda:decrypt_Mono())
decrypt_Mono_Button.pack(side = TOP)


inputString_Mono = Text(tab4,height=1,width=10)
inputString_Mono.pack(side = RIGHT)

label1 = Label(tab4,text="PlainText:")
label1.pack(side = RIGHT)

inputKey_Mono = Text(tab4,height=1,width=10)
inputKey_Mono.pack(side = RIGHT)

label2 = Label(tab4,text="Key:")
label2.pack(side = RIGHT)

output_Mono = Entry(tab4)
output_Mono.pack(side = BOTTOM)

output_Mono_Label = Label(tab4,text="Output:")
output_Mono_Label.pack(side = BOTTOM)



encrypt_Playfair_Button = Button(tab6,text = "Encrypt",command = lambda:encrypt_Playfair())
encrypt_Playfair_Button.pack(side = TOP)
decrypt_Playfair_Button = Button(tab6,text = "Decrypt",command=lambda:decrypt_Playfair())
decrypt_Playfair_Button.pack(side = TOP)


inputString_Playfair = Text(tab6,height=1,width=10)
inputString_Playfair.pack(side = RIGHT)

label1 = Label(tab6,text="PlainText:")
label1.pack(side = RIGHT)

inputKey_Playfair = Text(tab6,height=1,width=10)
inputKey_Playfair.pack(side = RIGHT)

label2 = Label(tab6,text="Key:")
label2.pack(side = RIGHT)

output_Playfair = Entry(tab6)
output_Playfair.pack(side = BOTTOM)

output_Playfair_Label = Label(tab6,text="Output:")
output_Playfair_Label.pack(side = BOTTOM)



encrypt_Hill_Button = Button(tab7,text="Encrypt",command=lambda:encrypt_Hill())
encrypt_Hill_Button.pack(side = TOP)
decrypt_Hill_Button = Button(tab7,text="Decrypt",command=lambda:decrypt_Hill())
decrypt_Hill_Button.pack(side = TOP)


inputString_Hill = Text(tab7,height=1,width=10)
inputString_Hill.pack(side = RIGHT)

label3 = Label(tab7,text="PlainText:")
label3.pack(side = RIGHT)

output_Hill = Entry(tab7,width=20)
output_Hill.pack(side = BOTTOM)

outputLabel = Label(tab7,text="Output")
outputLabel.pack(side = BOTTOM)

encrypt_Hill_Button_3x3 = Button(tab8,text="Encrypt",command=lambda:encrypt_Hill_3x3())
encrypt_Hill_Button_3x3.pack(side = TOP)
decrypt_Hill_Button_3x3 = Button(tab8,text="Decrypt",command=lambda:decrypt_Hill_3x3())
decrypt_Hill_Button_3x3.pack(side = TOP)

    

inputString_Hill_3x3 = Text(tab8,height=1,width=10)
inputString_Hill_3x3.pack(side = RIGHT)

label3 = Label(tab8,text="PlainText:")
label3.pack(side = RIGHT)

output_Hill_3x3 = Entry(tab8,width=20)
output_Hill_3x3.pack(side = BOTTOM)

outputLabel = Label(tab8,text="Output")
outputLabel.pack(side = BOTTOM)


tab_control.pack(expand=1, fill='both')

root.mainloop()