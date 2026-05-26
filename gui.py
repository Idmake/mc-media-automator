from tkinter import *
from tkinter import filedialog
import os
import script
from init_window import window
from custom_paths import load_custom_paths, save_custom_paths, CustomPath, PredefinedPath, load_paths, save_paths, FOLDER_PATH

# Load custom paths, if file exists
if load_paths: load_custom_paths()

class PathSelector:
    def __init__(self, description, row, pathvariable):
        label = Label(frame,   text=           description)
        entry = Entry(frame,   textvariable=   pathvariable, width=window.winfo_vrootwidth()) #TODO: Currently this only sets the width to a max value and doesn't dynamically change it.
        buttonBrowse = Button(frame,  text=         "browse",   command=lambda: self.set_pathvariable(      pathvariable=pathvariable))
        buttonClear = Button(frame,  text=          "clear",    command=lambda: self.clear_pathvariable(    pathvariable=pathvariable))

        frame.pack()
        label.grid(         row=row,    column=0,   padx=5, sticky="e")
        entry.grid(         row=row,    column=1,   padx=5)
        buttonBrowse.grid(  row=row,    column=2,   padx=5)
        buttonClear.grid(   row=row,    column=3,   padx=5)

        # How widgets should behave when the window is resized, in this case the entry width should increase with the window
        frame.columnconfigure(index=1, weight=1)

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
test1 = PathSelector(description="Minecraft.Client/Windows64Media/loc/",                row=1,  pathvariable=CustomPath.Windows64Media_loc)
test2 = PathSelector(description="Minecraft.Client/Windows64Media/",                    row=2,  pathvariable=CustomPath.Windows64Media)
test3 = PathSelector(description="Minecraft.Client/Common/Media/MediaWindows64.arc",    row=3,  pathvariable=CustomPath.MediaWindows64_arc)

buttonFrame =   Frame(window)
quitButton =    Button(buttonFrame, text="Quit", width=10, command=lambda: window.quit()).                                                              grid(row=0, column=0, padx=5, pady=10)
runButton =     Button(buttonFrame, text="Run",  width=10, command=lambda: script.run_script(CustomPath=CustomPath, PredefinedPath=PredefinedPath)).    grid(row=0, column=1, padx=5, pady=10)
buttonFrame.pack(anchor=SE, expand=True)

window.mainloop()

# Save paths after closing window
if save_paths: save_custom_paths()