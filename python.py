from tkinter import * 
from tkinter.ttk import * 
from open_file import *
  
#tkinter window
root = Tk()

root.title('Codificador EstudioVisual | Sin título')

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

# Create a multiline text area (Text widget)
text_area = Text(root, wrap=WORD, height=1000, width=1000)  # Adjust width and height as needed
text_area.pack(pady=10, padx=10)  # Adjust pady as needed for spacing

mainloop()