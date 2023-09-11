from tkinter import * 
from tkinter.ttk import * 
from open_file import select_file
  
#tkinter window
root = Tk()
root.title('Codificador EstudioVisual')

#setting window icon 
root.iconbitmap("icon.ico")
root.state("zoomed")
  
# Creating Menubar
menubar = Menu(root)


  
# File Menu
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Archivo', menu = file)
file.add_command(label ='Archivo Nuevo', command = None)
file.add_command(label ='Abrir Archivo', command = select_file)
file.add_command(label ='Guardar', command = None)
file.add_command(label ='Guardar Como', command = None)

# Help Menu
help = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Ayuda', menu = help)
help.add_command(label ='Acerca de', command = None)
  
# display Menu
root.config(menu = menubar)
mainloop()