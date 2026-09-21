import sys
import os
import traceback
import numpy
from pathlib import Path
import csv

#inputfile = Input("What file do you want to clean? ")
filecontents=[]

with open(inputfile, newline='') as csvfile:
    dareader = csv.DictReader(csvfile, delimiter=',')
    for row in dareader:
        filecontents.append(row)

print()