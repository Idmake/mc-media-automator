from tkinter import *
from tkinter import filedialog
import os
import script
from init_window import window
from custom_paths import load_custom_paths, save_custom_paths, CustomPath, PredefinedPath, load_paths, save_paths, FOLDER_PATH

# Load custom paths, if file exists
if load_paths: load_custom_paths()

class PathSelector(Frame):
    def __init__(self, description, pathvariable):
        Frame.__init__(self)
        self.pack(expand=Y, fill=BOTH)
        self.master.title("hello world")
        self.create_widgets()

    def create_widgets(self):
        Label(window, text="Select the paths to the following folders:").pack(pady=10, anchor=N)
        self.create_panel()

    def create_panel(self):
        panel = Frame(self)
        panel.pack(side=TOP, fill=BOTH, expand=Y)
        frame =         Frame(panel)
        label =         Label(frame, width=20, text="TEST LABEL")
        entry =         Entry(frame, width=25)
        buttonBrowse =  Button(frame, text="browse", command=lambda: print("browsing files"))
        buttonClear =   Button(frame, text="clear", command=lambda: print("im clear"))

        label.pack(side=LEFT)
        entry.pack(side=LEFT)
        buttonBrowse.pack(side=LEFT, padx=5)
        buttonClear.pack(side=LEFT, padx=5)
        frame.pack(fill=X, padx="1c", pady=3)

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
        


test1 = PathSelector(description="Minecraft.Client/Windows64Media/loc/",                  pathvariable=CustomPath.Windows64Media_loc)

"""
buttonFrame =   Frame(window)
quitButton =    Button(buttonFrame, text="Quit", width=10, command=lambda: window.quit()).                                                              grid(row=0, column=0, padx=5, pady=10)
runButton =     Button(buttonFrame, text="Run",  width=10, command=lambda: script.run_script(CustomPath=CustomPath, PredefinedPath=PredefinedPath)).    grid(row=0, column=1, padx=5, pady=10)
buttonFrame.pack(anchor=SE, expand=True)
"""

window.mainloop()

# Save paths after closing window
if save_paths: save_custom_paths()