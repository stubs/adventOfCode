#! /usr/bin/python
from collections import Counter
from itertools import chain

data = open('day3.txt', 'r').read().splitlines()

# part 1
collisions,  fabric = 0, dict()

for i in range(1000):
    fabric[i] = [[] for i in range(1000)]

for plan in data:
    plan_id = plan.split('@ ')[0].strip()
    start_index, key = [int(x) for x in plan.split('@ ')[1].split(': ')[0].split(',')]  # key = y-axis, start_index = x-axis
    width, height = [int(x) for x in plan.split('@ ')[1].split(': ')[1].split('x')]
    for h in range(key, key + height):
        for w in range(start_index, start_index + width):
            fabric[h][w].append(plan_id)

for val in fabric.values():
    for lst in val:
        if len(lst) > 1:
            collisions += 1
print(collisions)

# part 2
