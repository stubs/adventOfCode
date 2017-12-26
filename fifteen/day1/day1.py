filename = 'day1.txt'
# testdata = '(()))))'

def whatfloor(data):
    up = data.count('(')
    down =  data.count(')')

    print 'The data states Santa should go up ' + str(up) + ' floors.'
    print 'Then Santa should go down ' + str(down) + ' floors.'
    print 'Now I will subtract ' + str(down) + ' from ' + str(up) + ' to get my result of: ' + str(up - down)

# This one isn't working...ask about the while loop
def findbasement(testdata):
    curfloor = 0
    charpos = 0
    while curfloor > -1:
        for char in testdata:
            charpos += 1
            if char == '(':
                curfloor += 1
                # print curfloor
            elif char == ')':
                curfloor -= 1
                # print curfloor
    print charpos
findbasement(testdata)


#SOLUTION OPTION 1

#
# def findbasement(testdata):
#     curfloor = 0
#     charpos = 0
#     for char in testdata:
#         charpos += 1
#         if char == '(':
#             curfloor += 1
#         if char == ')':
#             curfloor -= 1
#         if curfloor < 0:
#             print charpos
#             break
#     print charpos
#
# findbasement(testdata)

#SOLUTION OPTION 2
# curfloor = 0
# charpos = 1
# with open(filename) as f:
#     while True:
#         c = f.read(1)
#         if not c:
#             break
#         if c == '(':
#             curfloor += 1
#             # print curfloor
#         elif c == ')':
#             curfloor -= 1
#             # print curfloor
#         if curfloor < 0:
#             print 'Character position is ' + str(charpos)
#             break
#         charpos += 1

# print 'Character position is ' + str(charpos)
