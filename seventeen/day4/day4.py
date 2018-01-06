#!/usr/bin/env python

import re

def part1(in_file):
    regex_pattern = re.compile(r'(\b\w+\b\s?).*\1')
    fin = open(in_file, 'r').readlines()
    total_lines = len(fin)

    for line in fin:
        if re.search(regex_pattern, line):
            total_lines -= 1

    return total_lines

#def part2():
