import tkinter.filedialog

#file selector function
def select_file():

    #declare permitted filetypes (so far only .txt)
    filetypes = (
        [("Text files", "*.txt")] 
    )

    #select file
    file = tkinter.filedialog.askopenfilename(filetypes=filetypes)
    return file