import csv

tri_data = []
true_tris = []
fake_tris = []

with open('day3.csv', 'r') as infile:
    data = csv.reader(infile)
    for row in data:
        tri_data.append(row[0].split())

for x in tri_data:
    for i,v in enumerate(x):
        x[i] = int(v)
    x = sorted(x)
    if x[0] + x[1] <= x[2]:
        if x not in fake_tris:
            fake_tris.append(x)
    else:
        if x not in true_tris:
            true_tris.append(x)

print len(true_tris)
