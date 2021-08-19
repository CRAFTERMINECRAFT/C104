import csv

with open("new.csv", newline = "") as f :
    c = csv.reader(f)
    l = list(c)

l.pop(0)

height = []

for i in range(len(l)):
    n = l[i][1]
    height.append(float(n))

height.sort()

lngth = len(height)

if lngth % 2 == 0:
    median1 = float(height[lngth//2])
    median2 = float(height[lngth//2 - 1])
    median = (median1 + median2)/2

else:
    median = height[lngth//2]

print(median)