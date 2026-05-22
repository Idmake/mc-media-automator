from tkinter import *
from tkinter import filedialog

window = Tk()
window.geometry("400x400")

class CustomPath:
    Windows64Media_loc =            StringVar(window, "D:/Games/MinecraftConsoles/Minecraft.Client/Windows64Media/loc")
    Windows64Media =                StringVar(window, "D:/Games/MinecraftConsoles/Minecraft.Client/Windows64Media")
    Common_Media =                  StringVar(window, "D:/Games/MinecraftConsoles/Minecraft.Client/Common/Media/")

window.mainloop()