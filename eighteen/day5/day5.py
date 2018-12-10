#! /usr/bin/python
import string
import sys

sys.setrecursionlimit(5000)

data = open('day5.txt', 'r').read().strip()

del_dict = dict()
for k, v in zip(string.ascii_lowercase, string.ascii_uppercase):
    del_dict[k] = v
for k, v in zip(string.ascii_uppercase, string.ascii_lowercase):
    del_dict[k] = v

def recur_checker(stringy):
    listy = list(stringy)
    del_count = 0
    for i in range(0, len(listy)):
        if len(listy[i:i+2]) == 2:
            if del_dict[listy[i]] == listy[i+1]:
                del listy[i+1]; del listy[i]
                del_count += 1

    if del_count == 0:
        return len(listy)
    else:
        return recur_checker(''.join(listy))

# part 1
print(recur_checker(data))

# part 2
polymer_lens = []
for i in string.ascii_lowercase:
    polymer_lens.append(recur_checker(data.replace(i,'').replace(i.upper(), '')))

print(min(polymer_lens))
