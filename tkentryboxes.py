# Entry is used to take input from the user.
# A box is provided on the interface where the text goes.
# this text can be retrieved and used by functions.
from tkinter import *

root = Tk()
root.geometry('200x150')

frame = Frame(root)
frame.pack()
# frame options: bg, bd, command, cursor, font, exportselection,
#fg, justify, relief, show, state, width, xscrollcommand,
# set, insert.
entry = Entry(frame, width= 20)
entry.insert(0, 'Username')
entry.pack(padx= 5, pady= 5)

entry1 = Entry(frame, width= 15)
entry1.insert(0, 'Password')
entry1.pack(padx= 5, pady= 5)

# In order to retrieve the input we must make a button
# to trigger the event.

def retrieve():
    print(entry.get())
    print(entry1.get())

button = Button(frame, text= 'Submit', command= retrieve)
button.pack(padx= 5, pady= 5)

root.mainloop()