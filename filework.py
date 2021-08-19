import csv

with open("new.csv", newline = "") as f :
    c = csv.reader(f)
    l = list(c)

l.pop(0)

height = []

for i in range(len(l)):
    n = l[i][1]
    height.append(float(n))

total = 0
for a in height:
    total = total + a

mean = total/len(height)
print(mean)