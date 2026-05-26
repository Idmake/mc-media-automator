import os
from tkinter import StringVar
from gui import window
from modify_file_funcs import file_readline, file_writeline

FOLDER_PATH = os.path.dirname(__file__).replace("\\", "/")
CUSTOM_PATHS_FILE_PATH = FOLDER_PATH + "/custom_paths.txt"
load_paths = True
save_paths = True



class CustomPath:
    Windows64Media_loc =            StringVar(window, "")
    Windows64Media =                StringVar(window, "")
    Common_Media =                  StringVar(window, "")

class PredefinedPath:
    mc_arc_util_master = FOLDER_PATH + "/mc-arc-util-master"
    MCLCE_StringTable_Compiler = FOLDER_PATH + "/MCLCE-StringTable-Compiler-Master"



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