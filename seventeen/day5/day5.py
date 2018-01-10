#!/usr/bin/env python

def part1(in_file):
    data = open("day5.txt", 'r').read().splitlines()
    data_len = len(data) - 1
    it_seed = 0
    move_count = 0
    while True:
        val = data[it_seed]
        data[it_seed] = str(int(val) + 1)
        it_seed += int(val)
        move_count += 1
        if it_seed < 0 or it_seed > data_len:
            break
    print(move_count)
