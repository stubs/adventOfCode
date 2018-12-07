#! /usr/bin/python

data = open('day3.txt', 'r').read().splitlines()

collisions, fabric, ids = 0, dict(), set()

for i in range(1000):
    fabric[i] = [[] for j in range(1000)]
for plan in data:
    plan_id = plan.split('@ ')[0].strip()
    ids.add(plan_id)
    start_index, key = [int(x) for x in plan.split('@ ')[1].split(': ')[0].split(',')]  # key = y-axis, start_index = x-axis
    width, height = [int(x) for x in plan.split('@ ')[1].split(': ')[1].split('x')]
    for h in range(key, key + height):
        for w in range(start_index, start_index + width):
            fabric[h][w].append(plan_id)

for val in fabric.values():
    for lst in val:
        if len(lst) > 1:
            collisions += 1
            for item in lst:
                if item in ids:
                    ids.remove(item)

print(collisions)           # part 1
print(ids)                  # part 2

