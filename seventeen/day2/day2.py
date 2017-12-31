#!/usr/bin/env python
import csv
import itertools


def pt1(fin):
    data = open(fin, 'r')
    csv_reader = csv.reader(data, delimiter="\t")
    row_diffs = []
    for row in csv_reader:
        min_ = min([int(num) for num in row])
        max_ = max([int(num) for num in row])
        diff = max_ - min_
        row_diffs.append(diff)
    return sum(row_diffs)

def pt2(fin):
    data = open(fin, 'r')
    csv_reader = csv.reader(data, delimiter="\t")
    row_diffs = []
    for row in csv_reader:
        combos = list(itertools.combinations(row, 2))
        for combo in combos:
            combo_min = min([int(num) for num in combo])
            combo_max = max([int(num) for num in combo])
            if combo_max % combo_min == 0:
                row_diffs.append(combo_max // combo_min)
    return sum(row_diffs)
