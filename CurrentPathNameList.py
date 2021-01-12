import os

path = "./"
files = os.listdir(path)

def writetxt(f):
    WriteFile = open("List.txt",'a')
    WriteFile.write(f)
    WriteFile.write('\n')
    WriteFile.close()

for f in files:
  fullpath = os.path.join(path, f)
  if os.path.isfile(fullpath):
    writetxt(f)
  elif os.path.isdir(fullpath):
    pass

