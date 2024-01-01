from tkinter import *
#creates frame object.
root = Tk()
# second way to set the size of the GUI, the geometry method cannot add color to the GUI.
root.geometry('500x400')
frame = Frame(root, bd= 10, bg='green', relief='sunken')
frame.pack()

'''THIS is where the label is!'''
# This is where the label will go.
# options include: anchor, bg, bd, bitmap, cursor, font,
# fg, height, image, justify, padx, pady, relief, text, 
#textvariable, underline, width, wraplength.
var = StringVar()
var.set('Hello World')
label = Label(frame, textvariable=var)
label.pack()

# Label button
def set():
    var.set('Good-Bye Cruel World')

button = Button(frame, text = 'set', command= set)
button.pack()
#make sure to title the GUI.
root.title('Frame with labels')
root.mainloop()