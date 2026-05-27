from tkinter import *
from tkinter import filedialog
import os
import script
from init_window import window
from custom_paths import load_custom_paths, save_custom_paths, CustomPath, PredefinedPath, load_paths, save_paths, FOLDER_PATH

# Load custom paths, if file exists
if load_paths: load_custom_paths()

#See https://pyinmyeye.blogspot.com/2012/08/tkinter-filedialog-demo.html?m=1 for reference
class PathSelector(Frame): 
    def __init__(self, description, pathvariable):
        Frame.__init__(self)
        self.pack()
        self.pathvariable = pathvariable
        self.description = description
        self.create_widgets()

    def create_widgets(self):
        Label(self, text=self.description).pack(pady=10)
        self.create_panel()

    def create_panel(self):
        panel = Frame(self)
        panel.pack()
        frame =         Frame(panel)
        entry =         Entry(frame, width=60, textvariable=self.pathvariable)
        buttonBrowse =  Button(frame, text="browse",    command=lambda: self.set_pathvariable(self.pathvariable))
        buttonClear =   Button(frame, text="clear",     command=lambda: self.clear_pathvariable(self.pathvariable))

        entry.pack(side=LEFT)
        buttonBrowse.pack(side=LEFT, padx=5)
        buttonClear.pack(side=LEFT, padx=5)
        frame.pack(padx="1c", pady=3)

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
        

Label(window, text="Select the paths to the following things:").pack(pady=3)

PathSelector(description="Minecraft.Client/Windows64Media/loc/",                pathvariable=CustomPath.Windows64Media_loc)
PathSelector(description="Minecraft.Client/Windows64Media/",                    pathvariable=CustomPath.Windows64Media)
PathSelector(description="Minecraft.Client/Common/Media/MediaWindows64.arc",    pathvariable=CustomPath.MediaWindows64_arc)

buttonFrame = Frame(window).pack(anchor=SE, expand=True)
Button(buttonFrame, text="Quit", width=10, command=lambda: window.quit()).                                                              grid(row=0, column=0, padx=5, pady=10)
Button(buttonFrame, text="Run",  width=10, command=lambda: script.run_script(CustomPath=CustomPath, PredefinedPath=PredefinedPath)).    grid(row=0, column=1, padx=5, pady=10)

window.mainloop()

# Save paths after closing window
if save_paths: save_custom_paths()