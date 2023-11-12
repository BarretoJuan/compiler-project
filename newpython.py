import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import Text

path = None

def create_tab():
    # Create a new tab
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Untitled")

    # Create a Text widget for text editing
    text_widget = Text(tab, undo=True)  # Enable undo functionality
    #text_widget.configure(encoding = "utf-8") # Allow utf-8 encoding so having accents and non english letters won't break
    text_widget.pack(fill="both", expand=True)

    wtf = notebook.index("end")
    # Bind Ctrl+Z and Ctrl+Y to undo and redo
    text_widget.bind("<Control-z>", lambda event: text_widget.edit_undo())
    text_widget.bind("<Control-y>", lambda event: text_widget.edit_redo())
    return text_widget # This should return the widget so we can use it as a text area


def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        global path
        path = file_path
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            file_name = file_path.split("/")[-1].split(".")[0]  # Extract the file name from the path
            text_widget = create_tab()
            text_widget.insert("1.0", content)
            notebook.tab(notebook.index("end") - 1, text=file_name)  # Change the tab label to the file name
        notebook.select(notebook.index("end") - 1)  # Switch to the newly created tab
        


def close_tab():
    # Get the currently selected tab
    current_tab = notebook.select()
    # Close the currently selected tab
    if current_tab:
        notebook.forget(current_tab)

def save_file():
    global path
    # Get the currently selected tab index
    current_tab_index = notebook.index(notebook.select())
    print("deberia ser un numero", current_tab_index)
    # Get the text widget from the currently selected tab
    text_widget = notebook.winfo_children()[current_tab_index].winfo_children()[0] # yeah, just dont ask me
    print("text mimimi", text_area)
    
    # Text file writing to save contents
    if path:
        with open(path, 'w') as file:
            content = text_widget.get(1.0, "end")
            file.write(content)
    else:
        print("No file path specified.")



root = tk.Tk()
root.title("Editor Estudio Visual")
root.state('zoomed')

# Create a Notebook widget for tabs
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Create the initial tab and bind the text_area created and bind it to a variable
text_area  = create_tab()

# Create a menu
menu = tk.Menu(root)
root.config(menu=menu)

# File menu
file_menu = tk.Menu(menu, tearoff = 0)
menu.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="Nueva Ventana", command= lambda: create_tab())
file_menu.add_command(label="Cerrar Ventana", command= lambda: close_tab())
file_menu.add_command(label="Abrir Archivo", command=open_file)
file_menu.add_command(label="Guardar", command=save_file)
file_menu.add_command(label="Guardar Como", command="")


file_menu.add_separator()
file_menu.add_command(label="Terminar programa", command=root.quit)

# compile_menu = tk.Menu(menu, tearoff=0)
# menu.add_cascade(label="Compilación", menu=compile_menu)
# compile_menu.add_command(label="Análisis Léxico", command="")


root.mainloop()

