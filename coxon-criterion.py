a = [7, 8, 3, 6]
b = [5, 1, 2, 3, 8]
c = []
t = []

for i in a:
    t.append(i)
    t.append(1)
    c.append(t)
    t = []

for i in b:
    t.append(i)
    t.append(2)
    c.append(t)
    t = []

c = sorted(c)

count = 1
for i in c:
    i.append(count)
    count += 1

temp = []
row = []

for i in range(len(c) - 1):
    if c[i][0] == c[i + 1][0]:
        row.append(c[i][-1])
        row.append(c[i + 1][-1])
        temp.append(row)
    if c[i][0] != c[i + 1][0] and c[i][0] == c[i - 1][0]:
        if c[i][-1] not in row:
            row.append(c[i][-1])
            temp.append(row)
        row = []


count = 0

for i in range(len(c) - 1):
    if c[i][0] == c[i + 1][0]:
        c[i][-1] = sum(temp[count]) / len(temp[count])
        c[i + 1][-1] = sum(temp[count]) / len(temp[count])
    if c[i][0] != c[i + 1][0] and c[i][0] == c[i - 1][0]:
        c[i - 1][-1] = sum(temp[count]) / len(temp[count])
        count += 1

R = 0

if len(b) < len(a):
    for i in c:
        if i[1] == 2:
            R += i[-1]

else:
    for i in c:
        if i[1] == 1:
            R += i[-1]

print(R)
# print(S)
print(temp)
print(c)
