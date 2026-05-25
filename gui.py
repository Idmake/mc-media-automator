from tkinter import *
from tkinter import filedialog
import os
import logic

load_paths = True
save_paths = True

FOLDER_PATH = os.path.dirname(__file__).replace("\\", "/")
CUSTOM_PATHS_FILE_PATH = FOLDER_PATH + "/custom_paths.txt"

window = Tk()
window.geometry("540x400")

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

class PredefinedPath:
    mc_arc_util_master = FOLDER_PATH + "/mc-arc-util-master"
    MCLCE_StringTable_Compiler = FOLDER_PATH + "/MCLCE-StringTable-Compiler-Master"

# Load custom paths, if file exists
if load_paths: load_custom_paths()

class PathSelector:
    def __init__(self, description, row, pathvariable):
        label = Label(frame,   text=           description)
        entry = Entry(frame,   textvariable=   pathvariable)
        buttonBrowse = Button(frame,  text=           "browse",   command=lambda: self.set_pathvariable(      pathvariable=pathvariable))
        buttonClear = Button(frame,  text=           "clear",    command=lambda: self.clear_pathvariable(    pathvariable=pathvariable))

        frame.pack()
        label.grid(         row=row,    column=0,   padx=5, sticky="E")
        entry.grid(         row=row,    column=1,   padx=5)
        buttonBrowse.grid(  row=row,    column=2,   padx=5)
        buttonClear.grid(   row=row,    column=3,   padx=5)

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
        
title = Label(window, text="Select the paths to the following folders:").pack(pady=10)

frame = Frame(window)
test1 = PathSelector(description="Minecraft.Client/Windows64Media/loc/",   row=1,  pathvariable=CustomPath.Windows64Media_loc)
test2 = PathSelector(description="Minecraft.Client/Windows64Media/",       row=2,  pathvariable=CustomPath.Windows64Media)
test3 = PathSelector(description="Minecraft.Client/Common/Media/",         row=3,  pathvariable=CustomPath.Common_Media)

buttonFrame =   Frame(window, bg="red")
quitButton =    Button(buttonFrame, text="Quit", width=10, command=lambda: window.quit()).                                                              grid(row=0, column=0, padx=5, pady=10)
runButton =     Button(buttonFrame, text="Run",  width=10, command=lambda: logic.run_script(CustomPath=CustomPath, PredefinedPath=PredefinedPath)).     grid(row=0, column=1, padx=5, pady=10)
buttonFrame.pack(anchor=SE, expand=True)

window.mainloop()

# Save paths after closing window
if save_paths: save_custom_paths()