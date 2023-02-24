
a = [285.72602517126484,
283.82628355967074,
240.9730677554637,
283.42858453370366,
287.09992184402336

]


b = [274.32406513259923,
278.48896135570067,
227.00537123301447,
280.3544687754745,
240.66805240618504

]

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

m = 5
n = 5

left = int(((m * (m + n + 1) - 1) / 2) - 1.644854 * ((m * n * (m + n + 1)) / 12) ** 0.5 )
right = m * (m + n + 1) - left
print(left, right)

# 2.326348
# 1.281552
# 3.090232
# 2.575829
# 1.644854
# 1.959964