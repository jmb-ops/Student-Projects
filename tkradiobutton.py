# Radio button GUI.
from tkinter import *

root = Tk()
root.geometry('200x150')
frame = Frame(root)
frame.pack()

var = IntVar()
# Radio button. cannot undo once selected.
Rbutton = Radiobutton(frame, text = 'option1', variable= var, value= 1)
Rbutton.pack(pady=20)

# retrieve button.
def retrieve():
    print(var.get())

button = Button(frame, text = "Submit", command = retrieve)
button.pack()

root.mainloop()