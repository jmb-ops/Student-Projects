# this section aims to modify the GUI frame and title.
'''To make an application with a GUI you must import tkinter'''
from tkinter import *
# create an object using the tkinter module.
root = Tk()
# create the frame and set root as parameter, use other options to customize.
# options include: bg, bd, width, heigth, cursor, highlightbackground,
# highlightcolor, highlightthickness, relief.

''' This is where the frame modification takes place'''
frame = Frame(root, relief= 'raised', cursor='dot', bg= 'green', width=500, height=400)
# you must use pack() or the GUI will not show up.
frame.pack()

# title() gives the GUI its title.
root.title('GUI frames')

# must use mainloop() to create the GUI.
root.mainloop()