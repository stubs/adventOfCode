#! /usr/bin/python
from collections import Counter

data = open('day4.txt', 'r').read().splitlines() # thank you vim for sorting the data!

guard_dict, minute_dict = dict(), dict()
for obs in data:
    date_time, info = obs.replace('[', '').split('] ')
    if info.split()[-1] == 'shift':
        curr_guard = info.split()[1]
        if not guard_dict.get(curr_guard):
            guard_dict[curr_guard] = []
    elif info.split()[-1] == 'asleep':
        guard_dict[curr_guard].append(int(date_time.split(':')[1]))
        if not minute_dict.get(int(date_time.split(':')[1])):
            minute_dict[int(date_time.split(':')[1])] = []
        minute_dict[int(date_time.split(':')[1])].append(curr_guard)
    else:
        sleep_start = guard_dict[curr_guard][-1]
        sleep_end = int(date_time.split(':')[1])
        for min in range(sleep_start + 1, sleep_end):
            if not minute_dict.get(min):
                minute_dict[min] = []
            guard_dict[curr_guard].append(min)
            minute_dict[min].append(curr_guard)

# part 1
_, sleepiest = max((len(v), k) for k, v in guard_dict.items())
min_counts = Counter(guard_dict[sleepiest])
mode_min = int(max(min_counts.keys(), key=(lambda k: min_counts[k])))

print('{} * {} = {}'.format(sleepiest,
                            mode_min,
                            int(sleepiest[1:]) * mode_min))

# part 2
max_how_often = ('',0, 0)
for k, v in minute_dict.items():
    sleeper_id = max(Counter(v), key= lambda k: Counter(v)[k])
    how_often = Counter(v)[sleeper_id]
    if how_often > max_how_often[1]:
        max_how_often = (sleeper_id, how_often, k)

print('{} * {} = {}'.format(max_how_often[0],
                            max_how_often[2],
                            int(max_how_often[0][1:]) * max_how_often[2]))
