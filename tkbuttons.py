# this module emphasizes the buttons option.
from tkinter import *
#creates frame object.
root = Tk()
# a fast way to set the size of the frame.
root.geometry('500x400')
frame = Frame(root)
frame.pack()

# Label
label = Label(frame, text= 'Intro to Buttons')
# make sure to pack it to the GUI.
label.pack()

''' This is where the Buttons will go!'''
# This is the button function def.
def button_click():
    print('Hello World')
# Button() options: activebackground, activeforeground, 
#bg='str_Color', bd= int, command = executes function, fg, font,
# height, heightcolor, image, justify, padx, pady, relief,
# state, underline, width, wraplength. 
button = Button(frame, text='Button1', command= button_click, fg='green', bg='orange', relief='raised')
button.pack(pady= 15)


#make sure to title the GUI.
root.title('Frame with Button!')
root.mainloop()