a = [50, 41, 45, 12, 74, 56]
b = [13, 78, 50, 50, 46, 70, 90]
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

for i in range(len(c) - 1):
    if c[i][0] == c[i + 1][0]:
        temp.append(c[i][-1])

    if c[i][0] != c[i + 1][0] and c[i][0] == c[i - 1][0]:
        temp.append(c[i][-1])

S = int(sum(temp) / len(temp))


for i in range(len(c) - 1):
    if c[i][0] == c[i + 1][0]:
        c[i][-1] = S

    if c[i][0] != c[i + 1][0] and c[i][0] == c[i - 1][0]:
        c[i][-1] = S


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
print(S)
print(temp)
print(c)