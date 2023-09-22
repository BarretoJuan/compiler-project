from tkinter import *
from tkinter import messagebox 
from tkinter.ttk import * 
import tkinter.filedialog
from platform import os

def check_file_last_mod():
    with open(file_path, 'r') as file:
        content = file.read()
        text_in_editor = text_area.get(1.0, END)
        if content != text_in_editor:
            return True
        else:
            return False

def check_file_last_mod_on_exit():
    if file_path:
        if check_file_last_mod():
            if messagebox.askyesno("Salir", "¿Deseas guardar los cambios?"):
                save_file()
                root.destroy()
            else:
                root.destroy()
        else:
            root.destroy()
    else:
        if text_area.get(1.0, END) != "\n":
            if messagebox.askyesno("Salir", "¿Deseas guardar los cambios?"):
                save_file_as()
                root.destroy()
            else:
                root.destroy()
        else:
            root.destroy()
#create new file function
def create_new_file():
    global file_path
    # Permitted filetypes
    filetypes = [("Text files", "*.txt")]

    # Save as dialog to create a new file
    new_file_path = tkinter.filedialog.asksaveasfilename(filetypes=filetypes)

    # Check if the user actually selected a file
    if new_file_path:
        file_path = new_file_path  # Update file_path with the selected path
        if not file_path.endswith(".txt"):
            file_path += ".txt"  # Add ".txt" extension if not provided
        try:
            #creates the file
            with open(file_path, 'x') as file:
                content = ""
        except FileExistsError:
            # Handle the case where the file already exists
            messagebox.showinfo("File Already Exists", "Este archivo ya existe, ábrelo para manipularlo")
            return

        text_area.delete(1.0, tkinter.END)
        text_area.insert(tkinter.INSERT, content)
        text_area.get(1.0, tkinter.END)

        # Update the window title
        root.title('Codificador EstudioVisual | ' + str(file_path) if file_path else 'Codificador EstudioVisual | Sin título')

#file selector function
def select_file():
    #declare permitted filetypes (so far only .txt)
    global file_path
    filetypes = ([("Text files", "*.txt")])

    #open file selector dialog
    file_path = tkinter.filedialog.askopenfilename(filetypes=filetypes)
    file_found = False
    #text file reading and insertion to the text area
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            file_found = True

    if file_found == True:
        text_area.delete(1.0, END) 
        text_area.insert(INSERT, content)
        text_area.get(1.0, END)
        #update main window title
        root.title('Codificador EstudioVisual | '+ str(file_path))

#save file function
def save_file():
    global file_path
    #text file writing to save contents
    if file_path:
        with open(file_path, 'w') as file:
            content = text_area.get(1.0, END)
            file.write(content)

#create new file function
def save_file_as():
    global file_path
    # Permitted filetypes
    filetypes = [("Text files", "*.txt")]

    # Save as dialog to create a new file
    new_file_path = tkinter.filedialog.asksaveasfilename(filetypes=filetypes)
    content = text_area.get(1.0, END)

    # Check if the user actually set a file to be created
    if new_file_path:
        file_path = new_file_path  # Update file_path with the selected path
        if not file_path.endswith(".txt"):
            file_path += ".txt"  # Add ".txt" extension if not provided
        try:
            with open(file_path, 'x') as file:
                pass
        except FileExistsError:
            # Handle the case where the file already exists
            messagebox.showinfo("File Already Exists", "Este archivo ya existe, ábrelo para manipularlo")
            return
        with open(file_path, 'w') as file:
            file.write(content)

        text_area.delete(1.0, tkinter.END)
        text_area.insert(tkinter.INSERT, content)
        text_area.get(1.0, tkinter.END)

        # Update the window title
        root.title('Codificador EstudioVisual | ' + str(file_path) if file_path else 'Codificador EstudioVisual | Sin título')



#file path variable declaration
global file_path 
file_path = None
                 
#tkinter window
root = Tk()
root.title('Codificador EstudioVisual | Sin título' if not file_path else 'Codificador EstudioVisual | '+ str(file_path))
root.protocol("WM_DELETE_WINDOW", check_file_last_mod_on_exit)

if os.name == 'nt':
    #setting window icon 
    root.iconbitmap("icon.ico")
    root.state("zoomed")

  
#creating Menubar6
menubar = Menu(root)
  
#file Menu
selected_file = select_file
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Archivo', menu = file)
file.add_command(label ='Archivo Nuevo', command = create_new_file)
file.add_command(label ='Abrir Archivo', command = select_file)
file.add_command(label ='Guardar', command = save_file)
file.add_command(label ='Guardar Como', command = save_file_as)

#help Menu
help = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Ayuda', menu = help)
help.add_command(label ='Acerca de', command = None)
  
#display Menu
root.config(menu = menubar)

#multiline text area 
text_area = Text(root, wrap=WORD, height=1000, width=1000) 
text_area.pack(pady=10, padx=10) 
text_area.get(1.0, END)

root.mainloop()