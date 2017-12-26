#!/usr/bin/env python


def day1a(data_file):
    in_file = open(data_file, 'r').read()
    sum_these = []
    for idx, char in enumerate(in_file):
        if idx + 1 == len(in_file) and char == in_file[0]:                  # handle last index and wrap to start
            sum_these.append(int(char))
        elif char == in_file[idx + 1]:
            sum_these.append(int(char))
    return sum(sum_these)


def day1b(data_file):
    in_file = open(data_file, 'r').read()
    sum_these = []
    data_len = len(in_file)
    for idx, char in enumerate(in_file):
        if idx + 1 > data_len//2 and char == in_file[idx - data_len//2]:      # handle last index and wrap to start
            sum_these.append(int(char))
        elif idx + 1 == data_len//2 and char == in_file[-1]:
            sum_these.append(int(char))
        elif idx + 1 < data_len//2 and char == in_file[idx + data_len//2]:
            sum_these.append(int(char))
    return sum(sum_these)
