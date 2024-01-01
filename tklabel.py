# how to make a GUI with a label.
'''To make an application with a GUI you must import tkinter'''
from tkinter import *
# create an object using the tkinter module.
root = Tk()
# create the frame and set root as parameter.
# you must use pack() or the GUI will not show up.
frame = Frame(root)
frame.pack()

# create a label.
# options include: anchor, bg, bd, bitmap, cursor, font,
# fg, height, image, justify, padx, pady, relief, text, 
#textvariable, underline, width, wraplength.
label = Label(frame, text= 'Hello World')
label.pack()
# must use mainloop() to create the GUI.
root.mainloop()