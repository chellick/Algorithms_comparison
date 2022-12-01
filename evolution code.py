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
lst_fit = []
lst_fit_temp = []
best_individ = []
# >--------------------------------------------------------------------------------------------------------

def fitness(individ):
    return sum(individ)


for i in range(indiv):
    c1 = []
    for i in range(dlin):
        a = randint(0, 1)
        c1.append(a)
    population.append(c1)
print(population, "первая")
for i in population:
    lst_fit.append(fitness(i))



for i in lst_fit:
    if best <= i:
        best = i
        temp_index = lst_fit.index(i)
        best_individ.append(population[temp_index])

    temp_count_pr += i
count_str.append(temp_count_pr / indiv)
best_p.append(best)

for i in range((steps - 1) * indiv):  # Основной цикл создания популяций
    #  while countc < dlin:
# >--------------------------------------------------------------------------------------------------------
    fp = randint(0, len(population) - 1)  # Турнирный метод отбора родителей
    sp = randint(0, len(population) - 1)

    if lst_fit[fp] >= lst_fit[sp]:
        parent1 = population[fp]
    else:
        parent1 = population[sp]

    fp = randint(0, len(population) - 1)  # Турнирный метод отбора родителей
    sp = randint(0, len(population) - 1)

    if lst_fit[fp] >= lst_fit[sp]:
        parent2 = population[fp]
    else:
        parent2 = population[sp]

    # fp = population[randint(0, len(population) - 1)]  # выборка индивидов из массива population
    # sp = population[randint(0, len(population) - 1)]
# >--------------------------------------------------------------------------------------------------------
    rand = randint(0, dlin - 1)  # Метод выборки ребенка путем скрещивания частей генотипа родителей
    fh = parent1[:rand]  # first half
    sh = parent2[rand::]  # second half
    child = fh + sh

    for i in range(len(child)):  # Метод мутации
        rand = random()
        if rand <= 0.02:
            child[i] = 1 if child[i] == 0 else 0
    lst_fit_temp.append(fitness(child))
    sep_population.append(child)  # Добавление ребенка в список

 # >--------------------------------------------------------------------------------------------------------
    if len(population) == len(sep_population):
        for i in lst_fit_temp:
            if best <= i:
                best = i
                temp_index = lst_fit_temp.index(i)
                best_individ.append(sep_population[temp_index])

            temp_count_pr += i

        best_p.append(best)
        count_str.append(temp_count_pr / indiv)

        lst_fit = lst_fit_temp.copy()
        population = sep_population.copy()
        sep_population = []
        lst_fit_temp = []

    temp_count_pr = 0
    #  print(population, "популяция")

# >--------------------------------------------------------------------------------------------------------

for ex in range(len(count_str) + 1):
    count_str_x = list(range(1, ex + 1))

for ex in range(len(best_p) + 1):
    best_p_x = list(range(1, ex + 1))

best_individ = best_individ[::-1]
del best_individ[1:]

# >--------------------------------------------------------------------------------------------------------
print(count_str, 'count str ')
print(best_individ, 'best individ')
print(child, 'child')
# >--------------------------------------------------------------------------------------------------------

figure, axis = plt.subplots()
x = count_str_x
y = count_str
x1 = best_p_x
y1 = best_p
print(best_p, best_p_x)
axis.plot(x, y, linewidth=2.0)
axis.plot(x1, y1)
# axis.set(xlim=(0, len(best_p_x) + 1))

plt.show()

