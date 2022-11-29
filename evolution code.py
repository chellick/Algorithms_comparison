# from calendar import c
# from os import sep
from random import randint, random
import numpy as np
import matplotlib.pyplot as plt

temp_count_pr = 0
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
indiv = int(input("сколько хотите индивидов?  "))
dlin = int(input("длина индивидов  "))
steps = int(input("кол-во поколений  "))
sep_population = []
count_str_x = []
best_p = []
best_count = 0

for i in range(indiv):
    c1 = []
    for i in range(dlin):
        a = randint(0, 1)
        c1.append(a)
    population.append(c1)
print(population, "первая")

for i in population:
    temp_count_pr = temp_count_pr + sum(i)
    if best <= sum(i):
        best = sum(i)
count_str.append(temp_count_pr / indiv)
best_p.append(best)


for i in range((steps- 1) * indiv):  #  Основной цикл создания популяций
#  while countc < dlin:
    fp = population[randint(0, len(population) - 1)]  # Турнирный метод отбора родителей
    sp = population[randint(0, len(population) - 1)]
#>--------------------------------------------------------------------------------------------------------
    if sum(fp) >= sum(sp):
        parent1 = fp
    else:
        parent1 = sp

    fp = population[randint(0, len(population) - 1)] #  выборка индивидов из массива population
    sp = population[randint(0, len(population) - 1)]


    if sum(fp) >= sum(sp):
        parent2 = fp
    else:
        parent2 = sp

    fp = population[randint(0, len(population) - 1)]  # выборка индивидов из массива population
    sp = population[randint(0, len(population) - 1)]
#>--------------------------------------------------------------------------------------------------------
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
#>--------------------------------------------------------------------------------------------------------
    if len(population) == len(sep_population):
        for i in population:
            if best <= sum(i):
                best = sum(i)
            temp_count_pr += sum(i)

        # count_pr = temp_count_pr / indiv
        best_p.append(best)
        count_str.append(temp_count_pr / indiv)

        # count_str_x.append(num_generation)
        population = sep_population.copy()
        sep_population = []



    temp_count_pr = 0
    #  print(population, "популяция")
#>--------------------------------------------------------------------------------------------------------

for ex in range(len(count_str) + 1):
    count_str_x = list(range(1, ex + 1))
#  print(count_str_x, "len str x")
#  print(count_str, "пригодность")
print(child)



for ex in range(len(best_p) + 1):
    best_p_x = list(range(1, ex + 1))
# print(population)
# print(best_p, best_p_x, "best_count")
print(count_str, 'count str ') #  , count_str_x)
# print(num_generation, "num_generation")
#>--------------------------------------------------------------------------------------------------------

figure, axis = plt.subplots()


x = count_str_x
y = count_str
x1 = best_p_x
y1 = best_p
print(best_p,  best_p_x)
axis.plot(x, y, linewidth=2.0)
axis.plot(x1, y1)
axis.set(xlim = (0, len(best_p_x) + 1))


plt.show()
