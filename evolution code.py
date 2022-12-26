# from calendar import c
# from os import sep


import math
from random import randint, random
import numpy as np
import matplotlib.pyplot as plt

temp_count_fit = 0
child = []
# count = 0
# count2 = 0
best = 0
parent_one = []
parent_two = []
population = []
# countc = 0
count_str = []
count_individ = int(input("сколько хотите индивидов?  "))
len_individ = int(input("длина индивидов  "))
count_generations = int(input("кол-во поколений  "))
mutation_probability = float(input("вероятность мутации   "))
child_population = []
count_str_x = []
best_individ_array = []
# best_count = 0
population_fit = []
lst_fit_x = []
lst_fit_temp = []
best_individ = []
best_individ_x = []
limit_one = int(input("ограничение 1 "))
limit_two = int(input("ограничение 2 "))
best = -math.inf

# >--------------------------------------------------------------------------------------------------------
def function(x):
     return ((x** 2 + x - 11) ** 2 + (x + x ** 2 - 7) ** 2) * (-1)
# def function(x):
#     return -(x-2)**2

def fitness_one(indiv):
    s_individ = "".join(map(str, indiv))
    int_individ = int(s_individ, 2)
    float_individ = (int_individ / (2 ** len(indiv) - 1)) * (limit_two - limit_one) + limit_one
    float_individ_y = function(float_individ)
    return float_individ_y



def float_number(indiv):
    s_indiv = "".join(map(str, indiv))
    int_individ = int(s_indiv, 2)
    float_individ = (int_individ / (2 ** len(indiv) - 1)) * (limit_two - limit_one) + limit_one
    return float_individ
# >--------------------------------------------------------------------------------------------------------

for i in range(count_individ):
    num_individ = []
    for i in range(len_individ):
        a = randint(0, 1)
        num_individ.append(a)
    population.append(num_individ)



for i in population:
    population_fit.append(fitness_one(i))


for i in range(len(population_fit)):
    if best <= population_fit[i]:
        best = population_fit[i]
        index_ = i
    temp_count_fit += population_fit[i]

best_individ.append(population[index_])
count_str.append(temp_count_fit / count_individ)
best_individ_array.append(best)
best = -math.inf

# >--------------------------------------------------------------------------------------------------------
for i in range((count_generations - 1) * count_individ):  # Основной цикл создания популяций
    #  while countc < len_individ:
# >--------------------------------------------------------------------------------------------------------
    fp = randint(0, len(population) - 1)  # Турнирный метод отбора родителей
    sp = randint(0, len(population) - 1)

    if population_fit[fp] >= population_fit[sp]:
        parent_one = population[fp]
    else:
        parent_one = population[sp]

    fp = randint(0, len(population) - 1)  # Турнирный метод отбора родителей
    sp = randint(0, len(population) - 1)

    if population_fit[fp] >= population_fit[sp]:
        parent_two = population[fp]
    else:
        parent_two = population[sp]

    # fp = population[randint(0, len(population) - 1)]  # выборка индивидов из массива population
    # sp = population[randint(0, len(population) - 1)]
# >--------------------------------------------------------------------------------------------------------
    rand = randint(0, len_individ - 1)  # Метод выборки ребенка путем скрещивания частей генотипа родителей
    fh = parent_one[:rand]  # first half
    sh = parent_two[rand::]  # second half
    child = fh + sh

    for i in range(len(child)):  # Метод мутации
        rand = random()
        if rand <= mutation_probability:
            child[i] = 1 if child[i] == 0 else 0
    lst_fit_temp.append(fitness_one(child))
    child_population.append(child)  # Добавление ребенка в список

# >--------------------------------------------------------------------------------------------------------
    best = -math.inf
    if len(population) == len(child_population):
        for i in range(len(population_fit)):
            if best <= lst_fit_temp[i]:
                best = lst_fit_temp[i]
                index_ = i
            temp_count_fit += lst_fit_temp[i]

        best_individ_array.append(best)
        count_str.append(temp_count_fit / count_individ)
        best_individ.append(child_population[index_])

        population_fit = lst_fit_temp.copy()
        population = child_population.copy()
        child_population = []
        lst_fit_temp = []
        best = -math.inf
    temp_count_fit = 0
    #  print(population, "популяция")

    # print(population)

# >--------------------------------------------------------------------------------------------------------

for ex in range(len(count_str) + 1):
    count_str_x = list(range(1, ex + 1))


for i in best_individ:
    best_individ_x.append(float_number(i))


# >--------------------------------------------------------------------------------------------------------
print(count_str, 'count str ')
print(best_individ, 'best_y count_individ')
print(child, 'child')
# >--------------------------------------------------------------------------------------------------------
figure, axis = plt.subplots()
x_one = np.linspace(limit_one, limit_two, 50)
y_one = [function(i) for i in x_one]
x = best_individ_x
y = best_individ_array

plt.scatter(x, y, 20)
axis.plot(x_one, y_one)
plt.show()
print(x , 'x')
print(y, 'y')
