
COUNT = 0

def chunker_two(iterable):
    leng = len(iterable)
    return [(v,iterable[i+1]) for i, v in enumerate(iterable) if i + 1 < leng]

for num in range(193651,649729):
    str_num = str(num)
    try:
        assert len(str_num) == 6 and all(True if tup[0] <= tup[1] else False for tup in chunker_two(str_num))
    except AssertionError:
        continue

    for char in '0123456789':
        occ = [i for i, v in enumerate(str_num) if v == char]
        if len(occ) > 1 and any(True for tup in chunker_two(occ) if tup[0]-tup[1] == -1):
            COUNT += 1
            break

# part 1
print(COUNT)


