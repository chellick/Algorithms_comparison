import math
from random import randint, random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

temp_count_fit = 0  # Среднее значение float в итерации
child = []  # Ребёнок
best = 0  # Сравнительная переменная (min\max)
parent_one = []  # 1 Участник в генерации потомка
parent_two = []  # 2 Участник в генерации потомка
population = []  # Оснвной массив популяции
count_str = []
final_x = -math.inf
final_y = -math.inf

count_individ = int(input("сколько хотите индивидов?  "))
len_individ = int(input("длина индивидов  "))
count_generations = int(input("кол-во поколений  "))
mutation_probability = float(input("вероятность мутации   "))
child_population = []
count_str_x = []
best_individ_array = []
population_fit = []
lst_fit_x = []
lst_fit_temp = []
best_individ = []
best_individ_x_one = []
best_individ_x_two = []
limit_one = int(input("ограничение 1 "))
limit_two = int(input("ограничение 2 "))
best = -math.inf


# >--------------------------------------------------------------------------------------------------------
def function(x1, x2):
    # return -((x1 ** 2) + (x2 ** 2))
    # return -(((x1 ** 2) + 2) - ((x2 ** 2) + 2))                                 # Задание фунции
    return np.cos(x1 + x2)
    # return -np.sin(10 * (x1 ** 2 + x2 ** 2))

def fitness_one(indiv):  # Значение Y (Z)
    s_indiv = "".join(map(str, indiv))
    int_individ_one = int(s_indiv[:len(s_indiv) // 2 + 1], 2)
    int_individ_two = int(s_indiv[len(s_indiv) // 2:], 2)

    float_individ_one = (int_individ_one / (2 ** (len(indiv) / 2) - 1)) * (limit_two - limit_one) + limit_one
    float_individ_two = (int_individ_two / (2 ** (len(indiv) / 2) - 1)) * (limit_two - limit_one) + limit_one  # Значение

    # print(float_individ_one, float_individ_two)

    float_individ_y = function(float_individ_one, float_individ_two)
    return float_individ_y


def float_number(indiv):  # Tuple X1, X2 (X, Y)
    s_indiv = "".join(map(str, indiv))
    int_individ_one = int(s_indiv[:len(s_indiv) // 2 + 1], 2)
    int_individ_two = int(s_indiv[len(s_indiv) // 2:], 2)

    float_individ_one = (int_individ_one / (2 ** (len(indiv) / 2) - 1)) * (limit_two - limit_one) + limit_one
    float_individ_two = (int_individ_two / (2 ** (len(indiv) / 2) - 1)) * (limit_two - limit_one) + limit_one

    return float_individ_two, float_individ_one


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
    best_individ_x_one.append(float_number(i)[0])
    best_individ_x_two.append(float_number(i)[1])


extra_val_index = []
for i in range(len(best_individ_x_two)):
    if best_individ_x_two[i] < limit_one or best_individ_x_two[i] > limit_two:
        extra_val_index.append(i)
extra_val_index = extra_val_index[::-1]
for i in extra_val_index:
    best_individ_x_one.pop(i)
    best_individ_x_two.pop(i)
    best_individ_array.pop(i)

# >--------------------------------------------------------------------------------------------------------


fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

x1 = best_individ_x_one
y1 = best_individ_x_two
z1 = best_individ_array
# size = 100
ax.scatter(y1, x1, z1, s=100)


ax.set_xlim3d(limit_one, limit_two)
ax.set_ylim3d(limit_one, limit_two)



# print(x1, '\n', y1, '\n', z1)

x = np.arange(limit_one, limit_two, 0.2)
y = np.arange(limit_one, limit_two, 0.2)

x, y = np.meshgrid(y, x)
z = function(y, x)

surf = ax.plot_surface(y, x, z, cmap=cm.Greys, linewidth=0, antialiased=False)

plt.xlabel('x', fontsize=6)
plt.ylabel('y', fontsize=6)

plt.xlim(limit_one, limit_two)
plt.ylim(limit_one, limit_two)

plt.show()

