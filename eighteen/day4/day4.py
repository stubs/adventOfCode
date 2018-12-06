#! /usr/bin/python
from collections import Counter

data = open('day4.txt', 'r').read().splitlines() # thank you vim for sorting the data!

guard_dict = dict()
for obs in data:
    date_time, info = obs.replace('[', '').split('] ')
    if info.split()[-1] == 'shift':
        curr_guard = info.split()[1]
        if not guard_dict.get(curr_guard):
            guard_dict[curr_guard] = []
    elif info.split()[-1] == 'asleep':
        guard_dict[curr_guard].append(int(date_time.split(':')[1]))
    else:
        sleep_start = guard_dict[curr_guard][-1]
        sleep_end = int(date_time.split(':')[1])
        for min in range(sleep_start + 1, sleep_end):
            guard_dict[curr_guard].append(min)

_, sleepiest = max((len(v), k) for k, v in guard_dict.items())

min_counts = Counter(guard_dict[sleepiest])
mode_min = int(max(min_counts.keys(), key=(lambda k: min_counts[k])))

print('{} * {} = {}'.format(sleepiest,
                            mode_min,
                            int(sleepiest[1:]) * mode_min))
