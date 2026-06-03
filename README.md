# Minecraft: Legacy Console Edition Media automator
This tool automates the process of renaming names or descriptions in Minecraft: Legacy Console Edition.
It combines both [MCLCE-StringTable-Compiler](https://github.com/codeHusky/MCLCE-StringTable-Compiler) and [mc-arc-util-master](https://github.com/nullptrref/mc-arc-util/)
into one project.

### What do I need?
- Node.js (for MCLCE-StringTable-Compiler)
- Python (at least Python 3.0, check your version using ```python --version```)

### How do I use it?
When you use a new ID (IDS_EXAMPLE or IDS_DESC_EXAMPLE) in your project:
- Open ```Windows64Media/loc/stringsGeneric.xml```
- Define what text (value) you want to display for the ID (you can use the other IDS as a reference).
- Save the file
- Open this project and run ```main.py```.

You don't need to edit ```strings.h``` itself, as the program generates it and your new IDs with it anyway.

### I ran into an problem.
Check the output window for information, if it isn't clear what happened or you've found a bug, consider opening an issue.

# Credits
[Luki](https://github.com/codeHusky) - MCLCE-StringTable-Compiler  
[Miku-666](https://github.com/nullptrref) - mc-arc-util-master  
[Stefan](https://github.com/Idmake)  
