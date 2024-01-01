# how to make a basic frame GUI (just an empty box).
'''To make an application with a GUI you must import tkinter'''
from tkinter import *
# create an object using the tkinter module.
root = Tk()
# create the frame and set root as parameter.
frame = Frame(root)
# you must use pack() or the GUI will not show up.
frame.pack()
# must use mainloop() to create the GUI.
root.mainloop()