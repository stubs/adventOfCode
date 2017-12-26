#!/usr/bin/env python
import csv

with open("day1.csv", "r") as infile:
    dir_list = list(csv.reader(infile))
    dir_list = dir_list[0]

for i, v in enumerate(dir_list):
    dir_list[i] = str(v).strip() #remove whitespace

x = 0
y = 0
orientation = 'N'

for i,v in enumerate(dir_list):
    if orientation == "N":
        if v[0] == "R":
            x += int(v[1:])
            orientation = "E"
        elif v[0] == "L":
            x -= int(v[1:])
            orientation = "W"
    elif orientation == "S":
        if v[0] == "R":
            x -= int(v[1:])
            orientation = "W"
        elif v[0] == "L":
            x += int(v[1:])
            orientation = "E"
    elif orientation == "E":
        if v[0] == "R":
            y -= int(v[1:])
            orientation = "S"
        elif v[0] == "L":
            y += int(v[1:])
            orientation = "N"
    elif orientation == "W":
        if v[0] == "R":
            y += int(v[1:])
            orientation = "N"
        elif v[0] == "L":
            y -= int(v[1:])
            orientation = "S"

print abs(x) + abs(y)
