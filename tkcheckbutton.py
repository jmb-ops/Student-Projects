# Check button GUI.
# Shows a predifined set of options.
from tkinter import *

root = Tk()
root.geometry("200x150")

frame = Frame(root)
frame.pack()

# This makes the check box.
# make sure to comment out below for option 2.
var = IntVar()

checkbox = Checkbutton(frame, text= 'option1', variable = var)
checkbox.pack(pady= 15)

# there are two ways to retrieve the data from the check box.
# the button method.
def retrieve():
    print(var.get())

button = Button(frame, text = "Submit", command = retrieve)
button.pack(padx = 5, pady = 5)

#option 2 no button.
#def retrieve():
    #print(var.get())

#checkbox = Checkbutton(frame, text= 'option1', variable = var, command= retrieve)
#checkbox.pack(pady= 15)

root.mainloop()