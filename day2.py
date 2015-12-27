#------Day 2 --------
filename = 'day2.txt'

cum_total_area = 0
ribbon_total = 0

def surfacearea(length, width, height):
    leng_area = length * width
    wid_area = width * height
    h_area = length * height

    area = 2*leng_area + 2*wid_area + 2*h_area + min(leng_area, wid_area, h_area)

    if min(leng_area, wid_area, h_area) == leng_area:
        ribbon = (2*length) + (2*width)
    elif min(leng_area, wid_area, h_area) == wid_area:
        ribbon = (2*width) + (2*height)
    else:
        ribbon = (2*length) + (2*height)

    ribbon += (length * width * height)

    return area , ribbon


with open(filename, 'r') as F:
    for i in F:
        l, w, h = i.split('x')
        area, ribbon = surfacearea(int(l), int(w), int(h))
        cum_total_area += area 
        ribbon_total += ribbon

print "Elves will need " + str(cum_total_area) + " square feet of wrapping paper."        
print "They are also going to need " + str(ribbon_total) + " feet of ribbon."
# ------------------------------------
