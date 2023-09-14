from tkinter import * 
from tkinter.ttk import * 
import tkinter.filedialog

#file path variable declaration
global file_path 
file_path = None

#file selector function
def select_file():
    #declare permitted filetypes (so far only .txt)
    global file_path
    filetypes = (
        [("Text files", "*.txt")] 
    )

    #open file selector dialog
    file_path = tkinter.filedialog.askopenfilename(filetypes=filetypes)

    #text file reading and insertion to the text area
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
    text_area.delete(1.0, END) 
    text_area.insert(INSERT, content)
    #update main window title
    root.title('Codificador EstudioVisual | '+ str(file_path))
  
#tkinter window
root = Tk()
root.title('Codificador EstudioVisual | Sin título' if not file_path else 'Codificador EstudioVisual | '+ str(file_path))


#setting window icon 
root.iconbitmap("icon.ico")
root.state("zoomed")
  
#creating Menubar
menubar = Menu(root)
  
#file Menu
selected_file = select_file
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Archivo', menu = file)
file.add_command(label ='Archivo Nuevo', command = None)
file.add_command(label ='Abrir Archivo', command = select_file)
file.add_command(label ='Guardar', command = None)
file.add_command(label ='Guardar Como', command = None)

print(select_file)
#help Menu
help = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Ayuda', menu = help)
help.add_command(label ='Acerca de', command = None)
  
#display Menu
root.config(menu = menubar)

#multiline text area 
text_area = Text(root, wrap=WORD, height=1000, width=1000) 
text_area.pack(pady=10, padx=10) 

root.mainloop()