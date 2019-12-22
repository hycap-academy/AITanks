from os import listdir
from os.path import isfile
AIPlayers = []
for f in  listdir():
    if isfile(f):
        if "AI" in f:
            name =f.replace("AI", "").replace(".py", "")
            AIPlayers.append([name, f])

print(AIPlayers)

#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

#or you could use os.walk() which will yield two lists for each directory it visits - splitting into files and dirs for you. If you only want the top directory you can just break the first time it yields

from os import walk

f = []
for (dirpath, dirnames, filenames) in walk(""):
    f.extend(filenames)
    break