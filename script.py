def run_script(CustomPath, PredefinedPath):
    import subprocess
    import os
    import zipfile
    import tkinter.messagebox

    def execute_command(args, shell):
        returnCode = subprocess.run(args=args, shell=shell).returncode
        error_upon_failure(returnCode)

    def error_upon_failure(returnCode):
        if returnCode != 0:
            subprocess.run(f"echo:", shell=True)
            subprocess.run(f"echo Command failed to execute.", shell=True)
            subprocess.run(f"echo:", shell=True)
            tkinter.messagebox.showerror(message=f"An unknown error occurred; check the output for more information if possible.")
            raise ValueError(f"Error code {returnCode}")
        
    def set_directory(path):
        os.chdir(path=path)


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
        execute_command(f"python arc2zip.py {FILE_PATH.MEDIAWINDOWS64_ARC}", shell=True)

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
        print("\n[WARNING] MediaWindows64.arc will be replaced with a new version, make sure to create a backup before you continue.")
        execute_command(f"pause", shell=True)
        execute_command(f"xcopy out.arc \"{FILE_PATH.MEDIAWINDOWS64_ARC}\" /Y /-I", shell=True)



    build_languages()
    replace_strings()
    convert_arc_to_zip()
    modify_zip()
    convert_zip_to_arc()
    replace_mediawindows64_arc()