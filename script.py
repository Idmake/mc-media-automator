import subprocess
import os
import zipfile
import tkinter.messagebox
from class_vars_funcs import get_class_stringvars, get_class_vars
from invalid_path_funcs import get_invalid_path_index

def error_upon_failure(returnCode):
    if returnCode != 0:
        subprocess.run(f"echo:", shell=True)
        subprocess.run(f"echo Command failed to execute.", shell=True)
        subprocess.run(f"echo:", shell=True)
        tkinter.messagebox.showerror(message=f"An unknown error occurred!\nPlease check if you have inserted the correct paths.")
        raise ValueError(f"Error code {returnCode}") #TODO: Write this to a file called "traceback.txt", so the output doesn't get clogged

def execute_command(args, shell):
    returnCode = subprocess.run(args=args, shell=shell).returncode
    error_upon_failure(returnCode)

def set_directory(path):
    os.chdir(path=path)

def run_script(CustomPath, PredefinedPath):

    custompaths = get_class_stringvars(CustomPath)
    invalid_path_index = get_invalid_path_index(custompaths)

    if invalid_path_index != -1:
        if custompaths[invalid_path_index] == "":       tkinter.messagebox.showerror(message=f"An empty path at index {invalid_path_index} was found.")
        else:                                           tkinter.messagebox.showerror(message=f"Invalid path \"{custompaths[invalid_path_index]}\" at index {invalid_path_index}.")

        return False
    


    
    # xcopy "source file" "destination file" /Y /-I
    # xcopy "source file" "destination folder" /Y /I
    # erase "source file"


    def build_languages():
        print("BUILDING LANGUAGES")

        # Create new languages.loc and strings.h files
        set_directory(PredefinedPath.MCLCE_StringTable_Compiler)
        execute_command(f"npm i", shell=True)
        execute_command(f"node index.js build languages.loc --folder {CustomPath.Windows64Media_loc.get()}", shell=True)

    def replace_strings():
        print("REPLACING STRINGS FILE")
        set_directory(PredefinedPath.MCLCE_StringTable_Compiler)
        execute_command(f"xcopy strings.h \"{CustomPath.Windows64Media.get()}\" /Y /-I", shell=True)

    def get_languages_path():
        print("GETTING LANGUAGES PATH")
        print (f"{PredefinedPath.MCLCE_StringTable_Compiler + "/" + "languages.loc"}")
        return f"{PredefinedPath.MCLCE_StringTable_Compiler + "/" + "languages.loc"}" 
        
    def convert_arc_to_zip():
        print("CONVERTING ARC TO ZIP")
        set_directory(PredefinedPath.mc_arc_util_master)
        execute_command(f"python arc2zip.py {CustomPath.MediaWindows64_arc.get()}", shell=True)

    def modify_zip():
        print("MODIFIYING ZIP")
        set_directory(PredefinedPath.mc_arc_util_master)
        tempName = "temp.zip"
        zipName = "arc.zip"    

        # Zipfile doesn't allow replacing or deleting files, so we copy the original
        # MediaWindows64.arc and recreate every file except "lanugages.loc". 
        # We "copy" the languages.loc file which was made earlier.
        # This mimics the action of replacing a file but comes at the cost of being a fucking headache
        
        execute_command(f"xcopy \"{zipName}\" \"{tempName}\" /Y /-I", shell=True)
        with zipfile.ZipFile(file=tempName, mode="r") as tempzip:
            with zipfile.ZipFile(file=zipName, mode="w", compression=zipfile.ZIP_DEFLATED) as zip:
                # "Copy" the created languages.loc to the destination inside the zip.
                # Destination should and needs to be in ANSI, otherwise the game will freeze.
                # Recreate any other file.
                for file in tempzip.filelist:
                    if (file.filename == "languages.loc"):
                        destination = "languages.loc"  
                        sourcePath = get_languages_path()                           
                        zip.write(sourcePath, destination)
                    else:
                        zip.writestr(file, tempzip.read(file.filename))
                        


    def convert_zip_to_arc():
        print("CONVERTING ZIP TO ARC")
        set_directory(PredefinedPath.mc_arc_util_master)
        execute_command(f"python zip2arc.py arc.zip", shell=True)

    def replace_mediawindows64_arc():
        print("REPLACING MEDIAWINDOWS64 ARC FILE")
        set_directory(PredefinedPath.mc_arc_util_master)
        execute_command(f"xcopy out.arc \"{CustomPath.MediaWindows64_arc.get()}\" /Y /-I", shell=True)



    build_languages()
    replace_strings()
    convert_arc_to_zip()
    modify_zip()
    convert_zip_to_arc()
    replace_mediawindows64_arc()
    tkinter.messagebox.showinfo(message=f"File was replaced successfully.", icon="info")