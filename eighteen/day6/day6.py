#! /usr/bin/python
import string

data = open('day6.txt', 'r').read().splitlines()
step_set = {i for i in string.ascii_uppercase}
direction_dict, ord_step_list = dict(), list()

for i in data:
    step_set.discard(i.split()[-3])
    if i.split()[1] not in direction_dict:
        direction_dict[i.split()[1]] = [i.split()[-3]]
    else:
        direction_dict[i.split()[1]].append(i.split()[-3])

indep_steps = sorted(step_set)
ord_step_list.append(indep_steps[0])

for k, val in direction_dict.items():
    for ind, step in enumerate(sorted(val)):
        if ind == 0:
            ord_step_list.append(step)
        else:
            if step < min(direction_dict[ord_step_list[-1]]):
                ord_step_list.append(step)
            else:
                ord_step_list.append(min(direction_dict[ord_step_list[-1]]))        # TODO fire at 'D':["A",...]



print(direction_dict)

