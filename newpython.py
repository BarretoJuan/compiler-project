import tkinter as tk
from tkinter import ttk

def create_tab():
    # Create a new tab
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Untitled")

    # Create a Text widget for text editing
    text_widget = tk.Text(tab, undo=True)  # Enable undo functionality
    text_widget.pack(fill="both", expand=True)

    # Bind Ctrl+Z and Ctrl+Y to undo and redo
    text_widget.bind("<Control-z>", lambda event: text_widget.edit_undo())
    text_widget.bind("<Control-y>", lambda event: text_widget.edit_redo())

def close_tab():
    # Get the currently selected tab
    current_tab = notebook.select()
    print(current_tab)

    # Close the currently selected tab
    if current_tab:
        notebook.forget(current_tab)



root = tk.Tk()
root.title("Editor Estudio Visual")
root.state('zoomed')

# Create a Notebook widget for tabs
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Create the initial tab
create_tab()

# Create a menu
menu = tk.Menu(root)
root.config(menu=menu)

# File menu
file_menu = tk.Menu(menu, tearoff = 0)
menu.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="Nueva Ventana", command=create_tab)
file_menu.add_command(label="Cerrar Ventana", command=close_tab)
file_menu.add_command(label="Guardar", command=root.quit)
file_menu.add_separator()
file_menu.add_command(label="Terminar programa", command=root.quit)


compile_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Compilación", menu=compile_menu)
compile_menu.add_command(label="Análisis Léxico", command=create_tab)

root.mainloop()
