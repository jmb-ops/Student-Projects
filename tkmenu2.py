# an enhanced menu with drop down options.
from tkinter import *

def emptyfunc():
    pass

root = Tk()

mainmenu = Menu(root)

# menu 1
# make sure to use the tearoff=0 to keep the menu on the same page.
filemenu = Menu(mainmenu, tearoff= 0)
filemenu.add_command(label = 'save', command= emptyfunc)
filemenu.add_command(label = 'exit', command= root.destroy)
mainmenu.add_cascade(label='File', menu= filemenu)

#menu 2
toolmenu = Menu(mainmenu, tearoff = 0)
toolmenu.add_command(label = 'debugger', command= emptyfunc)
mainmenu.add_cascade(label="Tools", menu=toolmenu)

# must use the root config or else menu wont display.
root.config(menu = mainmenu)
root.mainloop()
