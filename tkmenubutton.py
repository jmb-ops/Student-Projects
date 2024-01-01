# how to make a menu with buttons.
from tkinter import *

root = Tk()
root.geometry('200x150')
frame = Frame(root)
frame.pack()

menu_button = Menubutton(frame, text= 'Select your food', relief= RAISED)

var = IntVar()

Menu1 = Menu(menu_button, tearoff= 0)

Menu1.add_checkbutton(label= 'pizza', variable= var)

menu_button['menu'] = Menu1

menu_button.pack()
root.mainloop()