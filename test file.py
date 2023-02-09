import numpy as np
import random
import plotly.express as px
import math
import plotly.graph_objects as go
import copy



# num_particles = int(input('Количество точек '))
# population = []
# part_cord_array = []
# lim1 = int(input('Первый лимит '))
# lim2 = int(input('Второй лимит '))
# best_position = -math.inf
# index_p = 0
# iterations = int((input('Количество итераций ')))
# Omega = 0.72984
# Phi_p = 1
# Phi_g = 1
# count = 0
# # velocity = random.uniform(-(lim2 - lim1), lim2 - lim1)
# velocity = 0
#
# # > --------------------------------------------------------------------
#
# def function(x1, y1):
#     # return -np.sin(10 * (x1 ** 2 + y1 ** 2))
#     # return -(x1 ** 2 + y1 ** 2)
#     return 0.1 * x1 ** 2 + 0.1 * y1 ** 2 - 4 * np.cos(0.8 * x1) - 4 * np.cos(0.8 * y1) + 8
#
# for i in range(num_particles):
#     population.append([])
#
#
#
# def fitnes_swarm(swarm):  # лучшая позиция точки
#     best_s_position = -math.inf
#     for particle in swarm:
#         for r in particle:
#             if r[2] > best_s_position:
#                 best_s_position = r[2]
#                 best_r = r
#     return best_r
#
#
#
# def fitness_particle(particle):
#     best_p_position = -math.inf
#     for p in particle:
#         if p[2] > best_p_position:
#             best_p_position = p[2]
#             best_p = p
#     return best_p
#
#
#
#
#
# velocity_x = 0
# velocity_y = 0
#
# # > --------------------------------------------------------------------
# # начальная позиция точек
# temp_tuple = []
# for p in population:
#     a = random.uniform(lim1, lim2)
#     b = random.uniform(lim1, lim2)
#     c = function(a, b)
#     d = velocity_x
#     e = velocity_y
#     temp_tuple = [a, b, c, d, e]
#     p.append(temp_tuple)
#     temp_tuple = []
#
#
#
#
#
#
#
# # > --------------------------------------------------------------------
# for f in range(iterations):
#     for i in range(len(population)):
#
#
#         velocity_x = population[i][count][3]
#         p_best_x = fitness_particle(population[i])[0]
#         p_gbest_x = fitnes_swarm(population)[0]
#         p_pos_x = population[i][count][0]
#
#
#         velocity_y = population[i][count][4]
#         p_best_y = fitness_particle(population[i])[1]
#         p_gbest_y = fitnes_swarm(population)[1]
#         p_pos_y = population[i][count][1]
#
#
#         velocity_up_x = Omega * velocity_x + Phi_p * random.random() * (p_best_x - p_pos_x) + Phi_g * random.random() * (p_gbest_x - p_pos_x)
#         velocity_up_y = Omega * velocity_y + Phi_p * random.random() * (p_best_y - p_pos_y) + Phi_g * random.random() * (p_gbest_y - p_pos_y)
#
#
#         temp_tuple.append(population[i][count][0] + velocity_up_x)
#         temp_tuple.append(population[i][count][1] + velocity_up_y)
#         temp_tuple.append(function(population[i][count][0] + velocity_up_x, population[i][count][1] + velocity_up_y))
#         temp_tuple.append(velocity_up_x)
#         temp_tuple.append(velocity_up_y)
#         population[i].append(temp_tuple)
#         temp_tuple = []
#
#         velocity_up_x = 0
#         velocity_y = 0
#         velocity_up_y = 0
#         velocity_x = 0
#
#
#
#
#     count += 1
#
#
# # > --------------------------------------------------------------------
#
# x = []
# y = []
# z = []
#
#
# for i in population:
#     x.append(fitness_particle(i)[0])
#     y.append(fitness_particle(i)[1])
#     z.append(fitness_particle(i)[2])
#
# # for i in population:
# #     x.append(i[-1][0])
# #     y.append(i[-1][1])
# #     z.append(i[-1][-1])
#
#
# # for a, b, c in zip(x, y, z):
# #     print(a, b, c, '\n')
# # > --------------------------------------------------------------------

#
# x = [1]
# y = [1]
# z = [1]
# fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers')])
#
# def f(x, y):
#     return np.sin(x) * (np.e ** ((1 - np.cos(y)) ** 2)) + np.cos(y) * np.e ** ((1 - np.sin(x)) ** 2) + (x - y) ** 2
#
# x1 = np.outer(np.linspace(-2 * np.pi, 2 * np.pi , 100), np.ones(100))
# y1 = x1.copy().T
# z1 = f(x1, y1)
# fig.add_trace(go.Surface(x=x1, y=y1, z=z1))
# fig.show()



import math
from random import randint, random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import plotly.express as px
import plotly.graph_objects as go
import sys

temp_count_fit = 0  # Среднее значение float в итерации
child = []  # Ребёнок
best = 0  # Сравнительная переменная (min\max)
parent_one = []  # 1 Участник в генерации потомка
parent_two = []  # 2 Участник в генерации потомка
population = []  # Оснвной массив популяции
count_str = []



count_individ = int(input("сколько хотите индивидов?  "))
len_individ = int(input("длина индивидов  "))
count_generations = int(input("кол-во поколений  "))
mutation_probability = float(input("вероятность мутации   "))
search_input = input('максимум или минимум?   ')
# final_x = -math.inf
# final_y = -math.inf
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
if search_input == 'максимум':
    best = -math.inf
elif search_input == 'минимум':
    best = math.inf
else:
    print(f'Incorrect type: {search_input}', '\n', 'Correct one: максимум \ минимум')
    sys.exit()



# >--------------------------------------------------------------------------------------------------------
def function(x1, x2):
    # return -((x1 ** 2) + (x2 ** 2))
    return -(((x1 ** 2) + 2) - ((x2 ** 2) + 2))                                 # Задание фунции
    # return np.cos(x1 + x2)
    # return -np.sin(10 * (x1 ** 2 + x2 ** 2))
    # return 0.1 * x1 ** 2 + 0.1 * x2 ** 2 - 4 * np.cos(0.8 * x1) - 4 * np.cos(0.8 * x2) + 8
    # return  ((x1 ** 2) + x2 - 11) ** 2 + (x1 + (x2 ** 2) - 7) ** 2
    # return -((x1 + x2) ** 2)
def fitness_one(indiv):  # Значение Y (Z)
    s_indiv = "".join(map(str, indiv))
    int_individ_one = int(s_indiv[:len(s_indiv) // 2], 2)
    int_individ_two = int(s_indiv[len(s_indiv) // 2:], 2)

    float_individ_one = (int_individ_one / (2 ** (len(indiv) / 2) - 1)) * (limit_two - limit_one) + limit_one
    float_individ_two = (int_individ_two / (2 ** (len(indiv) / 2) - 1)) * (limit_two - limit_one) + limit_one  # Значение

    # print(float_individ_one, float_individ_two)

    float_individ_y = function(float_individ_one, float_individ_two)
    return float_individ_y


def float_number(indiv):  # Tuple X1, X2 (X, Y)
    s_indiv = "".join(map(str, indiv))
    int_individ_one = int(s_indiv[:len(s_indiv) // 2], 2)
    int_individ_two = int(s_indiv[len(s_indiv) // 2:], 2)

    float_individ_one = (int_individ_one / (2 ** (len(indiv) / 2) - 1)) * (limit_two - limit_one) + limit_one
    float_individ_two = (int_individ_two / (2 ** (len(indiv) / 2) - 1)) * (limit_two - limit_one) + limit_one

    return float_individ_one, float_individ_two


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
    if search_input == 'максимум':
        if best <= population_fit[i]:
            best = population_fit[i]
            index_ = i
        temp_count_fit += population_fit[i]
    elif search_input == 'минимум':
        if best >= population_fit[i]:
            best = population_fit[i]
            index_ = i
        temp_count_fit += population_fit[i]

best_individ.append(population[index_])
count_str.append(temp_count_fit / count_individ)
best_individ_array.append(best)
if search_input == 'максимум':
    best = -math.inf
elif search_input == 'минимум':
    best = math.inf

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

    if search_input == 'максимум':
        best = -math.inf
    elif search_input == 'минимум':
        best = math.inf

    if len(population) == len(child_population):
        for i in range(len(population_fit)):
            if search_input == 'максимум':
                if best <= lst_fit_temp[i]:
                    best = lst_fit_temp[i]
                    index_ = i
                temp_count_fit += lst_fit_temp[i]
            elif search_input == 'минимум':
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
        if search_input == 'максимум':
            best = -math.inf
        elif search_input == 'минимум':
            best = math.inf
    temp_count_fit = 0

# >--------------------------------------------------------------------------------------------------------

for ex in range(len(count_str) + 1):
    count_str_x = list(range(1, ex + 1))

for i in best_individ:
    best_individ_x_one.append(float_number(i)[0])
    best_individ_x_two.append(float_number(i)[1])

# >--------------------------------------------------------------------------------------------------------

x1 = best_individ_x_one
y1 = best_individ_x_two
z1 = best_individ_array

fig = go.Figure(data=[go.Scatter3d(x=x1, y=y1, z=z1, mode='markers')])

x = np.outer(np.linspace(limit_one, limit_two, 100), np.ones(100))
y = x.copy().T
z = function(x, y)
fig.add_trace(go.Surface(x=x, y=y, z=z))
fig.show()