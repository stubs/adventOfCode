#! /usr/bin/python
import string

data = open('day6.txt', 'r').read().splitlines()
step_set = {i for i in string.ascii_uppercase}
direction_dict, ord_step_list = dict(), list()

for i in data:
    step_set.discard(i.split()[-3])
    if i.split()[-3] not in direction_dict:
        direction_dict[i.split()[-3]] = [i.split()[1]]
    else:
        direction_dict[i.split()[-3]].append(i.split()[1])

indep_steps = sorted(step_set)
ord_step_list.append(indep_steps.pop(0))

while len(ord_step_list) < 26:
    match_flag = False
    matches = []

    for k, val in direction_dict.items():
        if k in ord_step_list:
            pass
        elif all(step in ord_step_list for step in sorted(val)):
            matches.append(k)
            match_flag = True

    if match_flag:
        if indep_steps:
            if sorted(matches)[0] < indep_steps[0]:
                ord_step_list.append(sorted(matches)[0])
            else:
                ord_step_list.append(indep_steps.pop(0))
        else:
            ord_step_list.append(sorted(matches)[0])

    else:
        ord_step_list.append(indep_steps.pop(0))

print(''.join(ord_step_list))
