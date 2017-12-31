filename = 'day3.txt'


f = open(filename, 'r')
directions = f.read()
# Function that moves Santa about a cartesian plane. directions
# are going to be a long string.
def moveSanta(directions):
    x = 0
    y = 0
    yield x,y
    for direction in directions:
        if direction == '<':
            x -= 1
        elif direction == '>':
            x += 1
        elif direction == '^':
            y += 1
        elif direction == 'v':
            y -= 1
        yield x,y


def homes_visited(directions):
    lucky_homes = []
    kinda_lucky_homes = []
    for position in moveSanta(directions):
        # if position in kinda_lucky_homes and position in lucky_homes:
        #     lucky_homes.append(position)
        # if position in kinda_lucky_homes and position not in lucky_homes:
        #     lucky_homes.append(position)
        if position not in kinda_lucky_homes:
            kinda_lucky_homes.append(position)
    return len(kinda_lucky_homes)


    # lucky_homes =set([])
    # kinda_lucky_homes = set([])
    # for position in moveSanta(directions):
    #     if position in kinda_lucky_homes: #and position not in lucky_homes:
    #         lucky_homes.add(position)
    #     if position not in kinda_lucky_homes:
    #         kinda_lucky_homes.add(position)
    # # return len(kinda_lucky_homes) #houses that received only 1 present
    # return len(lucky_homes)# more than one   present

print homes_visited(directions) #test it!
