def run_script(CustomPath, PredefinedPath):
    import subprocess
    import os
    import zipfile

    def ExecuteCommand(args, shell):
        returnCode = subprocess.run(args=args, shell=shell).returncode
        ErrorUponFaliure(returnCode)

    def ErrorUponFaliure(returnCode):
        if returnCode != 0:
            subprocess.run(f"echo Command failed to execute. && pause", shell=True)
            subprocess.run(f"echo:", shell=True)
            subprocess.run(f"echo #### PYTHON TRACEBACK ####:", shell=True)
            subprocess.run(f"echo:", shell=True)
            raise ValueError(f"Error code {returnCode}")
        
    def SetDirectory(path):
        os.chdir(path=path)


    # xcopy "source file" "destination file" /Y /-I
    # xcopy "source file" "destination folder" /Y /I
    # erase "source file"


    def BuildLanguages():
        print("BUILDING LANGUAGES")

        # Create new languages.loc and strings.h files
        SetDirectory(PredefinedPath.MCLCE_StringTable_Compiler)
        ExecuteCommand(f"npm i", shell=True)
        ExecuteCommand(f"node index.js build languages.loc --folder {CustomPath.Windows64Media_loc.get()}", shell=True)

    def ReplaceStrings():
        print("REPLACING STRINGS FILE")
        SetDirectory(PredefinedPath.MCLCE_StringTable_Compiler)
        ExecuteCommand(f"xcopy strings.h \"{CustomPath.Windows64Media.get()}\" /Y /-I", shell=True)

    def GetLanguagesPath():
        print("GETTING LANGUAGES PATH")
        print (f"{PredefinedPath.MCLCE_StringTable_Compiler + "/" + "languages.loc"}")
        return f"{PredefinedPath.MCLCE_StringTable_Compiler + "/" + "languages.loc"}" 
        
    def ConvertArctoZip():
        print("CONVERTING ARC TO ZIP")
        SetDirectory(PredefinedPath.mc_arc_util_master)
        ExecuteCommand(f"python arc2zip.py {FILE_PATH.MEDIAWINDOWS64_ARC}", shell=True)

    def ModifyZip():
        print("MODIFIYING ZIP")
        SetDirectory(PredefinedPath.mc_arc_util_master)
        tempName = "temp.zip"
        zipName = "arc.zip"    

        # Zipfile doesn't allow replacing or deleting files, so we copy the original
        # MediaWindows64.arc and recreate every file except "lanugages.loc". 
        # We "copy" the languages.loc file which was made earlier.
        # This mimics the action of replacing a file but comes at the cost of being a fucking headache
        
        ExecuteCommand(f"xcopy \"{zipName}\" \"{tempName}\" /Y /-I", shell=True)
        with zipfile.ZipFile(file=tempName, mode="r") as tempzip:
            with zipfile.ZipFile(file=zipName, mode="w", compression=zipfile.ZIP_DEFLATED) as zip:
                # "Copy" the created languages.loc to the destination inside the zip.
                # Destination should and needs to be in ANSI, otherwise the game will freeze.
                # Recreate any other file.
                for file in tempzip.filelist:
                    if (file.filename == "languages.loc"):
                        destination = "languages.loc"  
                        sourcePath = GetLanguagesPath()                           
                        zip.write(sourcePath, destination)
                    else:
                        zip.writestr(file, tempzip.read(file.filename))
                        


    def ConvertZipToArc():
        print("CONVERTING ZIP TO ARC")
        SetDirectory(PredefinedPath.mc_arc_util_master)
        ExecuteCommand(f"python zip2arc.py arc.zip", shell=True)

    def ReplaceMediaWindows64Arc():
        print("REPLACING MEDIAWINDOWS64 ARC FILE")
        SetDirectory(PredefinedPath.mc_arc_util_master)
        print("\n[WARNING] MediaWindows64.arc will be replaced with a new version, make sure to create a backup before you continue.")
        ExecuteCommand(f"pause", shell=True)
        ExecuteCommand(f"xcopy out.arc \"{FILE_PATH.MEDIAWINDOWS64_ARC}\" /Y /-I", shell=True)



    BuildLanguages()
    ReplaceStrings()
    ConvertArctoZip()
    ModifyZip()
    ConvertZipToArc()
    ReplaceMediaWindows64Arc()