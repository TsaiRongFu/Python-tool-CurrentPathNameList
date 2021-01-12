import os

path = "./"
files = os.listdir(path)

def writetxt(f):
    WriteFile = open("List.txt",'a',encoding="utf-8")
    WriteFile.write(f)
    WriteFile.write('\n')
    WriteFile.close()

for f in files:
    fullpath = os.path.join(path, f)
    if os.path.isfile(fullpath):
        if f == "List.txt":
            pass
        elif f == "CurrentPathNameList.py":
            pass
        else:
            writetxt(f)
    elif os.path.isdir(fullpath):
        pass

