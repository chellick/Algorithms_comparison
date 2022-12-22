import numpy as np
import matplotlib.pyplot as plt
from random import randint, random


# a, b = map(float, input().split())
# c = float.bin(a)
# print(c)
limit1 = int(input("Введите ограничение "))
limit2 = int(input("Введите ограничение (второе)) "))



times_of_populations = 50
individ = 6
dlin = 6
population = []
child = []
best = []
best_count_temp = 0
best_pick = []
sep_population = []
count = 0
count2 = 0
b_list = []
result = []
for i in range(individ):
    c1 = []
    for i in range(dlin):
        a = randint(0, 1)
        c1.append(a)
    population.append(c1)
for i in population:
    if best_count_temp <= sum(i):
        best_pick = i
best.append(best_pick)

for i in range((times_of_populations - 1) * individ):
    fp = population[randint(0, len(population) - 1)]  # Турнирный метод отбора родителей
    sp = population[randint(0, len(population) - 1)]

    for i in fp:
        if i == 1:
            count += 1
    for i in sp:
        if i == 1:
            count2 += 1
    if count > count2:
        parent1 = fp
    elif count == count2:
        parent1 = fp
    else:
        parent1 = sp
    #  print(count, count2)
    count = 0
    count2 = 0

    fp = population[randint(0, len(population) - 1)]  # выборка индивидов из массива population
    sp = population[randint(0, len(population) - 1)]

    for i in fp:
        if i == 1:
            count += 1
    for i in sp:
        if i == 1:
            count2 += 1
    if count > count2:
        parent2 = fp
    elif count == count2:
        parent2 = fp
    else:
        parent2 = sp
    count = 0
    count2 = 0

    rand = randint(0, dlin - 1)  # Метод выборки ребенка путем скрещивания частей генотипа родителей
    fh = parent1[:rand]  # first half
    sh = parent2[rand::]  # second half
    child = fh + sh

    for i in range(len(child)):  # Метод мутации
        rand = random()
        if rand <= 0.02:
            child[i] = 1 if child[i] == 0 else 0

    sep_population.append(child)

    if len(population) == len(sep_population):
        for i in population:
            if best_count_temp <= sum(i):
                best_pick = i
        best.append(best_pick)


        population = sep_population.copy()
        sep_population = []
        best_pick = []
        print(population)


for num in best:
    s = (''.join(map(str, num)))
    s = int(s, 2)
    b_list.append(s)
# print(b_list)

for i in b_list:
    res = (i / 2 ** dlin)*(limit1 - limit2) + limit1
    result.append(res)


print(result)

# print(result)
# print(b_list)


# x_one = np.linspace(-10, 10, 50)
# y_one = [-(i**2) for i in x_one]
#
# fig, ax = plt.subplots()
# x = x_one
# y = y_one
# x2 = result
# y2 = [-(i**2) for i in x_one]
#
# ax.plot(x, y)
# ax.plot(x2, y2 , 'go')
#
#
# plt.xlim(limit_one, limit_two)
# plt.show()





