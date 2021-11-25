from tkinter import *
import tkinter as tk
from extended_euclid import extended_euclid

root = Tk()
root.geometry('300x300')

def retrieve_input():
    m = inputM.get("1.0","end-1c")
    b = inputB.get("1.0","end-1c")
    outputText.delete(0,"end")
    outputText.insert(0,extended_euclid(int(m),int(b)))
    

inputB = Text(root,height=1,width=3)
inputB.pack(side = RIGHT)

label1 = Label(root,text="b=")
label1.pack(side = RIGHT)

inputM = Text(root,height=1,width=3)
inputM.pack(side = RIGHT)

label2 = Label(root,text="m=")
label2.pack(side = RIGHT)

outputText = Entry(root)
outputText.pack(side = BOTTOM)


button = Button(root,text="Compute",command=lambda:retrieve_input())
button.pack(side = LEFT)

root.mainloop()