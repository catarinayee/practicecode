import sys
import os
import traceback
import numpy
from pathlib import Path

dirinput = input("What's the name of the target directory? ")
path = Path.cwd()
q = path / dirinput

pathlist = []


for child in q.iterdir():
    pathlist.append(child)

for p in pathlist:
    rightpath = Path(p)

    with rightpath.open('r', newline='') as f: 
        print(f)
        filereader = f.readlines()
        for line in filereader:
           print("yippee")


