#! python
from collections import Counter

data = open('day2.csv', 'r').read().splitlines()
sorted_data = sorted(data)

# part 1
twos, threes = 0, 0
for i in data:
    if 2 in Counter(i).values():
        twos += 1
    if 3 in Counter(i).values():
        threes += 1

check_sum =  twos * threes
print('Part 1 Answer: {}'.format(check_sum))


# part 2
def checker(lst):
    temp_list = lst[:]
    while len(temp_list) > 1:
        check = temp_list.pop()
        for i in temp_list:
            if len(check) == len(i):
                diffs, common = 0, ''
                for z in zip(check,i):
                    if z[0] != z[1]:
                        diffs += 1
                    else:
                        common += z[0]
                if diffs < 2:
                    print(('Part 2 Answer: {} === may be partner id to === {}\n'
                            'Common chars are ===> {}'.format(check, i, common)))

checker(sorted_data)
