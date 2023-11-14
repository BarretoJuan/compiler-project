import tkinter as tk
from tkinter import ttk, filedialog, Text

path = None

def create_tab():
    # Create a new tab
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Untitled")

    # Create a Text widget for text editing
    text_widget = Text(tab, undo=True)  # Enable undo functionality
    text_widget.pack(fill="both", expand=True)

    # Bind Ctrl+Z and Ctrl+Y to undo and redo
    text_widget.bind("<Control-z>", lambda event: text_widget.edit_undo())
    text_widget.bind("<Control-y>", lambda event: text_widget.edit_redo())
    return text_widget

def update_path(event):
    # Update the global path variable when a new tab is selected
    global path
    current_tab_index = notebook.index(notebook.select())
    path = notebook.tab(current_tab_index, "text")
    print("el path es "+path)

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
            notebook.tab(notebook.index("end") - 1, text=file_path)  # Change the tab label to the full file path
        notebook.select(notebook.index("end") - 1)  # Switch to the newly created tab

def close_tab():
    save_file()
    # Get the currently selected tab
    current_tab = notebook.select()
    # Close the currently selected tab
    if current_tab:
        notebook.forget(current_tab)

def save_file():
    global path
    # Get the currently selected tab index
    current_tab_index = notebook.index(notebook.select())
    # Get the text widget from the currently selected tab
    text_widget = notebook.winfo_children()[current_tab_index].winfo_children()[0]
    
    # Text file writing to save contents
    if path != 'Untitled':
        with open(path, 'w') as file:
            content = text_widget.get(1.0, "end")
            file.write(content)
            notebook.tab(current_tab_index, text=path)
    else:
        save_as()


def save_as():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        global path
        path = file_path
        save_file()

root = tk.Tk()
root.title("Editor Estudio Visual")
root.state('zoomed')

# Create a Notebook widget for tabs
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Bind the <<NotebookTabChanged>> event to update the path when a new tab is selected
notebook.bind("<<NotebookTabChanged>>", update_path)

# Create the initial tab and bind the text_area created and bind it to a variable
text_area = create_tab()

# Create a menu
menu = tk.Menu(root)
root.config(menu=menu)

# File menu
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="Nueva Ventana", command=lambda: create_tab())
file_menu.add_command(label="Cerrar Ventana", command=lambda: close_tab())
file_menu.add_command(label="Abrir Archivo", command=open_file)
file_menu.add_command(label="Guardar", command=save_file)
file_menu.add_command(label="Guardar Como", command=save_as)

file_menu.add_separator()
file_menu.add_command(label="Terminar programa", command=root.quit)

root.mainloop()
