def file_writeline(file, mode, line):
    with open(file, mode) as f:
        f.write(line+"\n")

def file_readline(file, line):
    with open(file, "r") as f:
        for i, ln in enumerate(f):
            if (i == line):
                return ln.strip("\n")
            
        print("failed to read line, is line", line, "out of bounds?")