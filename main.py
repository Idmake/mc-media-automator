from tkinter import *
from tkinter import filedialog

window = Tk()
window.geometry("400x400")

class CustomPath:
    Windows64Media_loc =            StringVar(window, "D:/Games/MinecraftConsoles/Minecraft.Client/Windows64Media/loc")
    Windows64Media =                StringVar(window, "D:/Games/MinecraftConsoles/Minecraft.Client/Windows64Media")
    Common_Media =                  StringVar(window, "D:/Games/MinecraftConsoles/Minecraft.Client/Common/Media/")

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
        if selected_path == "":
            return
        
        # We selected a path, set it.
        StringVar.set(pathvariable, selected_path)
        


test1 = PathSelector(description="hi",      pathvariable=CustomPath.Windows64Media_loc)
test2 = PathSelector(description="bye",     pathvariable=CustomPath.Windows64Media)

window.mainloop()