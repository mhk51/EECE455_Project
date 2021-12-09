from tkinter import *
import tkinter as tk
from tkinter import ttk
from encyptions import encryptaffinecipher,Encryptvigenere,decryptaffinecipher,Decryptvigenere,crackaffinecipher
from extended_euclid import extended_euclid
from monoalphabetic_cipher import encrypt_Monoalphabetic,decrypt_Monoalphabetic
from playfair import decryptPlayfair, encryptPlayfair
root = Tk()
root.geometry('600x400')


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


tab_control.add(tab2, text='Affine')
tab_control.add(tab5,text='Crack Affine')

tab_control.add(tab3, text='Vigenere')

tab_control.add(tab4,text = "Monoalphabetic")

tab_control.add(tab6,text = 'Playfair')

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
    output_Playfair.delete(0,"end")
    output_Playfair.insert(0,encryptPlayfair(plaintext,key))

def decrypt_Playfair():
    plaintext = inputString_Playfair.get("1.0","end-1c")
    key = inputKey_Playfair.get("1.0","end-1c")
    output_Playfair.delete(0,"end")
    output_Playfair.insert(0,decryptPlayfair(plaintext,key))



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



tab_control.pack(expand=1, fill='both')

root.mainloop()