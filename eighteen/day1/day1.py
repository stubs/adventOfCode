#! python
from itertools import cycle

data = open('day1.csv', 'r').read().splitlines()

# part 1
end_freq = sum(map(int, data))
print('Part 1 Answer: {}'.format(end_freq))

# part 2
def accumu(lis):
    sum_set = set()
    total = 0
    for x in cycle(map(int, lis)):
         total += x
         if total in sum_set:
             return total
         else:
             sum_set.add(total)


print('Part 2 Answer: {}'.format(accumu(data)))
