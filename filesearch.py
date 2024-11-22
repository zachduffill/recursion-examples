import os 

path = []

def list_to_path(l,q=""):
    return chr(92).join(l)+chr(92)+q

def walk(dir,q):
    path.append(dir)

    cwd = list_to_path(path)
    contents = os.listdir(cwd)

    files = []
    dirs = []
    for c in contents:
        if os.path.isdir(os.path.join(cwd,c)):
            dirs.append(c)
        else: files.append(c)

    for d in dirs:
        if walk(d,q):
            return True

    for f in files:
        if f==q: return True

    path.pop()
    return False

query = input("search: ")

cwd = os.getcwd()
if walk(cwd,query):
    print(list_to_path(path,query))
else:
    print("File not found")