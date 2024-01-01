# this is an label editing example. code explained below.
'''The code in the example above creates a button which calls a function when clicked.  
This function then changes the color of the label. You can edit more than just the color of the label, 
like it’s text for instance.'''
from tkinter import *

def changecolor():
    label.configure(fg = "blue")

root = Tk()
button = Button(root, text='Choose Color', command = changecolor).pack(pady=20)
label = Label(root, text = "Color", fg = "black")
label.pack()

root.geometry('180x160')
root.mainloop()
