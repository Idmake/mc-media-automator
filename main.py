from tkinter import *
from tkinter import filedialog

window = Tk()
window.geometry("400x400")

class CustomPath:
    Windows64Media_loc =            StringVar(window, "D:/Games/MinecraftConsoles/Minecraft.Client/Windows64Media/loc")
    Windows64Media =                StringVar(window, "D:/Games/MinecraftConsoles/Minecraft.Client/Windows64Media")
    Common_Media =                  StringVar(window, "D:/Games/MinecraftConsoles/Minecraft.Client/Common/Media/")

class PathSelector:
    def __init__(self, label_text):
        Label(window, text=label_text).pack()

test1 = PathSelector("hi")
test2 = PathSelector("this")
test3 = PathSelector("is")
test4 = PathSelector("cool")

window.mainloop()