from calendar import c
from os import sep
from random import randint, random
import numpy as np
import matplotlib.pyplot as plt

child = []
count = 0
count2 = 0
best = 0
space = ""
parent1 = []
parent2 = []
population = []
countc = 0
count_str = []
count_pr = 0
indiv = int(input("сколько хотите индивидов?  "))
dlin = int(input("длина индивидов  "))
steps = int(input("кол-во поколений  "))
sep_population = []
count_str_x = []
count_str.append(count_pr)
num_generation = 0
count_str_x.append(num_generation)
best_p = []
best_count = 0

for i in range(indiv):
    c1 = []
    for i in range(dlin):
        a = randint(0, 1)
        c1.append(a)
    population.append(c1)
print(population, "первая")
num_generation += 1
for i in range((steps- 1) * indiv):  #  Основной цикл создания популяций
#  while countc < dlin:
    fp = population[randint(0, len(population) - 1)]  #  Турнирный метод отбора родителей
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

    fp = population[randint(0, len(population) - 1)] #  выборка индивидов из массива population
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

    for i in range(len(child)):  #  Метод мутации
        rand = random()
        if rand <= 0.02:
            child[i] = 1 if child[i] == 0 else 0 
    """
    for i in child:  #  Нахождение количества едениц в генотипе ребёнка
        if i == 1:
            countc += 1
    count_str.append(countc)
    countc = 0

    #  print(countc, d)
    
    #  print(child, "child")
    """
    sep_population.append(child)  # Добавление ребенка в список
    #  print(sep_population, "changed population")
    #  print(population, " популяция ", sep_population, " дочерняя популяция ")
    
    if len(population) == len(sep_population):
        for i in population:
            count_pr = sum(i) / len(population)
            if best < sum(i):
                best = sum(i)
                best_p.append(i)
                best_count += 1
        count_str.append(count_pr)
        num_generation += 1
        count_str_x.append(num_generation)
        population = sep_population.copy()
        sep_population = []
        
    #  count_pr = 0
    #  print(population, "популяция")


for ex in range(len(count_str) + 1):
    count_str_x = list(range(1, ex + 1))
#  print(count_str_x, "len str x")
#  
#  print(count_str, "пригодность")
print(child)



for ex in range(len(best_p) + 1):
    best_p_x = list(range(1, ex + 1))
print(best_p, best_p_x, "best_count")
print(len(count_str), count_str_x)
print(num_generation, "num_generation")


figure, axis = plt.subplots(2)
x = count_str_x
y = count_str
x1 = best_p
y1 = best_p_x
axis[0].plot(x, y)
axis[1].plot(x1, y1)

plt.show()
