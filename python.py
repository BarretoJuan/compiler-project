# importing only  those functions 
# which are needed
from tkinter import * 
from tkinter.ttk import * 
from time import strftime
  
# creating tkinter window
root = Tk()
root.title('Codificador EstudioVisual')

#setting window icon 
root.iconbitmap("icon.ico")
root.state("zoomed")
  
# Creating Menubar
menubar = Menu(root)
  
# Adding File Menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Archivo', menu = file)
file.add_command(label ='Archivo Nuevo', command = None)
file.add_command(label ='Abrir Archivo', command = None)
file.add_command(label ='Guardar', command = None)
file.add_command(label ='Guardar Como', command = None)

# Adding Help Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Ayuda', menu = help_)
help_.add_command(label ='Acerca de', command = None)
  
# display Menu
root.config(menu = menubar)
mainloop()