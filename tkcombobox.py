# Combobox presents a drop down list of options and displays them one at a time.
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('200x150')

frame = Frame(root)
frame.pack()

# list of drop down options.
drop_list = ['option1', 'option2', 'option3']

combo = ttk.Combobox(frame, values = drop_list)
combo.set('Select an option')
combo.pack(pady= 20)
# must make a button with a get function to retrieve the data.
# or a way to do without a button refer to checkbutton.py
root.mainloop()