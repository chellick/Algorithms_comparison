
a = [46.28853791404259,
     46.28834092488858,
     46.28310080856807,
     46.2830760512917,
     46.2883219033007,
     46.28888374619194,
     46.287135070203774,
     46.28964210914915,
     46.28725227182834

     ]
b = [46.28218016683725,
     46.289169583350144,
     46.288812794787866,
     46.28834867055551,
     46.28754349781903,
     46.28853937586855,
     46.289584050807775,
     46.28971361901278,
     46.28824588658314

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

m = 10
n = 10

left = int(((m * (m + n + 1) - 1) / 2) - 1.959964 * ((m * n * (m + n + 1)) / 12) ** 0.5 )
right = m * (m + n + 1) - left
print(left, right)

# 2.326348
