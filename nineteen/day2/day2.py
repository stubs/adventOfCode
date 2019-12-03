#! /usr/bin/env python

# already replaced index 1, 2 with vals 12 and 2
DATA = '1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,1,10,23,27,2,27,13,31,1,31,6,35,2,6,35,39,1,39,5,43,1,6,43,47,2,6,47,51,1,51,5,55,2,55,9,59,1,6,59,63,1,9,63,67,1,67,10,71,2,9,71,75,1,6,75,79,1,5,79,83,2,83,10,87,1,87,5,91,1,91,9,95,1,6,95,99,2,99,10,103,1,103,5,107,2,107,6,111,1,111,5,115,1,9,115,119,2,119,10,123,1,6,123,127,2,13,127,131,1,131,6,135,1,135,10,139,1,13,139,143,1,143,13,147,1,5,147,151,1,151,2,155,1,155,5,0,99,2,0,14,0'
int_list = [int(num) for num in DATA.split(',')]

def part1(in_list):
    list_copy = in_list[:]
    for i, v in enumerate(list_copy):
        if i%4 == 0:
            if v == 1:
                list_copy[list_copy[i+3]] = list_copy[list_copy[i+1]] + list_copy[list_copy[i+2]]
            elif v == 2:
                list_copy[list_copy[i+3]] = list_copy[list_copy[i+1]] * list_copy[list_copy[i+2]]
            elif v == 99:
                return list_copy[0]

def part2(in_list, param1, param2):
    list_copy = in_list[:]
    list_copy[1], list_copy[2] = param1, param2
    return part1(list_copy)

# part 1
print(part1(int_list))

# part 2
for j in range(100):
    for k in range(99,-1,-1):
        if part2(int_list,j, k) == 19690720:
            print(100 * j + k)
