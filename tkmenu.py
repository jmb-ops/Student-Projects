# how to set up a menu GUI.
from tkinter import *

def save():
    pass

root = Tk()
root.geometry('200x150')
frame = Frame(root)
frame.pack()

# here is where the menue code is.
my_menu = Menu(frame)
my_menu.add_command(label = 'Save', command= save)
my_menu.add_command(label = 'Exit', command= root.destroy)
# must use root.config to assign menu object as menu for root window.
root.config(menu = my_menu)

root.mainloop()