from tkinter import *
from tkinter import filedialog
import os

load_paths = True
save_paths = True

FOLDER_PATH = os.path.dirname(__file__).replace("\\", "/")
CUSTOM_PATHS_FILE_PATH = FOLDER_PATH + "/custom_paths.txt"

window = Tk()
window.geometry("400x400")

def file_writeline(file, mode, line):
    with open(file, mode) as f:
        f.write(line+"\n")

def file_readline(file, line):
    with open(file, "r") as f:
        for i, ln in enumerate(f):
            if (i == line):
                return ln.strip("\n")
            
        print("failed to read line, is line", line, "out of bounds?")

def save_custom_paths():
    print("save/create custom paths file")

    # This file is so small, we can just override it
    file_writeline  (CUSTOM_PATHS_FILE_PATH, "w", CustomPath.Windows64Media_loc.get())
    file_writeline  (CUSTOM_PATHS_FILE_PATH, "a", CustomPath.Windows64Media.get())
    file_writeline  (CUSTOM_PATHS_FILE_PATH, "a", CustomPath.Common_Media.get())

def load_custom_paths():
    print("load custom paths file")

    if not os.path.exists(CUSTOM_PATHS_FILE_PATH): 
        print("no custom paths file found, skipping loading")
        return
    
    StringVar.set(CustomPath.Windows64Media_loc,    file_readline(CUSTOM_PATHS_FILE_PATH, 0))
    StringVar.set(CustomPath.Windows64Media,        file_readline(CUSTOM_PATHS_FILE_PATH, 1))
    StringVar.set(CustomPath.Common_Media,          file_readline(CUSTOM_PATHS_FILE_PATH, 2))

class CustomPath:
    Windows64Media_loc =            StringVar(window, "")
    Windows64Media =                StringVar(window, "")
    Common_Media =                  StringVar(window, "")

# Load custom paths, if file exists
if load_paths: load_custom_paths()

class PathSelector:
    def __init__(self, description, pathvariable):
        
        Label(window,   text=           description).pack(pady=10)
        Entry(window,   textvariable=   pathvariable).pack()
        Button(window,  text=           "browse",   command=lambda: self.set_pathvariable(      pathvariable=pathvariable)).pack()
        Button(window,  text=           "clear",    command=lambda: self.clear_pathvariable(    pathvariable=pathvariable)).pack()

    # Clear pathvariable associated with this instance
    def clear_pathvariable(self, pathvariable):
        StringVar.set(pathvariable, "")

    # Select a new path for the pathvariable
    def set_pathvariable(self, pathvariable):
        selected_path = filedialog.askopenfilename()

        # We didn't select anything, return
        if selected_path == "" or selected_path == None:
            return
        
        # We selected a path, set it.
        StringVar.set(pathvariable, selected_path)
        


test1 = PathSelector(description="hi",      pathvariable=CustomPath.Windows64Media_loc)
test2 = PathSelector(description="bye",     pathvariable=CustomPath.Windows64Media)
test3 = PathSelector(description="bye",     pathvariable=CustomPath.Common_Media)

window.mainloop()

# Save paths after closing window
if save_paths: save_custom_paths()