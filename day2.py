#------PROBLEM 1 --------
filename = 'day2.txt'

cum_total_area = 0

def surfacearea(length, width, height):
    leng_area = length * width
    wid_area = width * height
    h_area = length * height

    area = 2*leng_area + 2*wid_area + 2*h_area + min(leng_area, wid_area, h_area)
    return area 

with open(filename, 'r') as F:
    for i in F:
        l, w, h = i.split('x')
        cum_total_area += surfacearea(int(l),int(w),int(h))

print "Elves will need " + str(cum_total_area) + " square feet of wrapping paper."        
# ------------------------------------
