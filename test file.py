# import math
# from random import randint, random
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib as mpl
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import cm
# import plotly.express as px
# import plotly.graph_objects as go
# import sys
#
# temp_count_fit = 0  # Среднее значение float в итерации
# child = []  # Ребёнок
# best = 0  # Сравнительная переменная (min\max)
# parent_one = []  # 1 Участник в генерации потомка
# parent_two = []  # 2 Участник в генерации потомка
# population = []  # Оснвной массив популяции
# count_str = []
#
#
#
# count_individ = int(input("сколько хотите индивидов?  "))
# len_individ = int(input("длина индивидов  "))
# count_generations = int(input("кол-во поколений  "))
# mutation_probability = float(input("вероятность мутации   "))
# search_input = input('максимум или минимиум?   ')
# # final_x = -math.inf
# # final_y = -math.inf
# child_population = []
# count_str_x = []
# best_individ_array = []
# population_fit = []
# lst_fit_x = []
# lst_fit_temp = []
# best_individ = []
# best_individ_x_one = []
# best_individ_x_two = []
# limit_one = int(input("ограничение 1 "))
# limit_two = int(input("ограничение 2 "))
# if search_input == 'максимум':
#     best = -math.inf
# elif search_input == 'минимум':
#     best = math.inf
# else:
#     print(f'Incorrect type: {search_input}', '\n', 'Correct one: максимум \ минимум')
#     sys.exit()
#
#
#
# # >--------------------------------------------------------------------------------------------------------
# def function(x1, x2):
#     # return -((x1 ** 2) + (x2 ** 2))
#     # return -(((x1 ** 2) + 2) - ((x2 ** 2) + 2))                                 # Задание фунции
#     # return np.cos(x1 + x2)
#     # return -np.sin(10 * (x1 ** 2 + x2 ** 2))
#     # return 0.1 * x1 ** 2 + 0.1 * x2 ** 2 - 4 * np.cos(0.8 * x1) - 4 * np.cos(0.8 * x2) + 8
#     return  ((x1 ** 2) + x2 - 11) ** 2 + (x1 + (x2 ** 2) - 7) ** 2
#
# def fitness_one(indiv):  # Значение Y (Z)
#     s_indiv = "".join(map(str, indiv))
#     int_individ_one = int(s_indiv[:len(s_indiv) // 2], 2)
#     int_individ_two = int(s_indiv[len(s_indiv) // 2:], 2)
#
#     float_individ_one = (int_individ_one / (2 ** (len(indiv) / 2) - 1)) * (limit_two - limit_one) + limit_one
#     float_individ_two = (int_individ_two / (2 ** (len(indiv) / 2) - 1)) * (limit_two - limit_one) + limit_one  # Значение
#
#     # print(float_individ_one, float_individ_two)
#
#     float_individ_y = function(float_individ_one, float_individ_two)
#     return float_individ_y
#
#
# def float_number(indiv):  # Tuple X1, X2 (X, Y)
#     s_indiv = "".join(map(str, indiv))
#     int_individ_one = int(s_indiv[:len(s_indiv) // 2], 2)
#     int_individ_two = int(s_indiv[len(s_indiv) // 2:], 2)
#
#     float_individ_one = (int_individ_one / (2 ** (len(indiv) / 2) - 1)) * (limit_two - limit_one) + limit_one
#     float_individ_two = (int_individ_two / (2 ** (len(indiv) / 2) - 1)) * (limit_two - limit_one) + limit_one
#
#     return float_individ_one, float_individ_two
#
#
# # >--------------------------------------------------------------------------------------------------------
#
# for i in range(count_individ):
#     num_individ = []
#     for i in range(len_individ):
#         a = randint(0, 1)
#         num_individ.append(a)
#     population.append(num_individ)
#
# for i in population:
#     population_fit.append(fitness_one(i))
#
# for i in range(len(population_fit)):
#     if search_input == 'максимум':
#         if best <= population_fit[i]:
#             best = population_fit[i]
#             index_ = i
#         temp_count_fit += population_fit[i]
#     elif search_input == 'минимум':
#         if best >= population_fit[i]:
#             best = population_fit[i]
#             index_ = i
#         temp_count_fit += population_fit[i]
#
# best_individ.append(population[index_])
# count_str.append(temp_count_fit / count_individ)
# best_individ_array.append(best)
# if search_input == 'максимум':
#     best = -math.inf
# elif search_input == 'минимум':
#     best = math.inf
#
# # >--------------------------------------------------------------------------------------------------------
#
# for i in range((count_generations - 1) * count_individ):  # Основной цикл создания популяций
#     #  while countc < len_individ:
#
# # >--------------------------------------------------------------------------------------------------------
#
#     fp = randint(0, len(population) - 1)  # Турнирный метод отбора родителей
#     sp = randint(0, len(population) - 1)
#
#     if population_fit[fp] >= population_fit[sp]:
#         parent_one = population[fp]
#     else:
#         parent_one = population[sp]
#
#     fp = randint(0, len(population) - 1)  # Турнирный метод отбора родителей
#     sp = randint(0, len(population) - 1)
#
#     if population_fit[fp] >= population_fit[sp]:
#         parent_two = population[fp]
#     else:
#         parent_two = population[sp]
#
# # >--------------------------------------------------------------------------------------------------------
#
#     rand = randint(0, len_individ - 1)  # Метод выборки ребенка путем скрещивания частей генотипа родителей
#     fh = parent_one[:rand]  # first half
#     sh = parent_two[rand::]  # second half
#     child = fh + sh
#
#     for i in range(len(child)):  # Метод мутации
#         rand = random()
#         if rand <= mutation_probability:
#             child[i] = 1 if child[i] == 0 else 0
#     lst_fit_temp.append(fitness_one(child))
#     child_population.append(child)  # Добавление ребенка в список
#
# # >--------------------------------------------------------------------------------------------------------
#
#     if search_input == 'максимум':
#         best = -math.inf
#     elif search_input == 'минимум':
#         best = math.inf
#
#     if len(population) == len(child_population):
#         for i in range(len(population_fit)):
#             if search_input == 'максимум':
#                 if best <= lst_fit_temp[i]:
#                     best = lst_fit_temp[i]
#                     index_ = i
#                 temp_count_fit += lst_fit_temp[i]
#             elif search_input == 'минимум':
#                 if best <= lst_fit_temp[i]:
#                     best = lst_fit_temp[i]
#                     index_ = i
#                 temp_count_fit += lst_fit_temp[i]
#
#         best_individ_array.append(best)
#         count_str.append(temp_count_fit / count_individ)
#         best_individ.append(child_population[index_])
#
#         population_fit = lst_fit_temp.copy()
#         population = child_population.copy()
#         child_population = []
#         lst_fit_temp = []
#         if search_input == 'максимум':
#             best = -math.inf
#         elif search_input == 'минимум':
#             best = math.inf
#     temp_count_fit = 0
#
# # >--------------------------------------------------------------------------------------------------------
#
# for ex in range(len(count_str) + 1):
#     count_str_x = list(range(1, ex + 1))
#
# for i in best_individ:
#     best_individ_x_one.append(float_number(i)[0])
#     best_individ_x_two.append(float_number(i)[1])
#
# # >--------------------------------------------------------------------------------------------------------
#
# x1 = best_individ_x_one
# y1 = best_individ_x_two
# z1 = best_individ_array
#
# fig = go.Figure(data=[go.Scatter3d(x=x1, y=y1, z=z1, mode='markers')])
#
# x = np.outer(np.linspace(limit_one, limit_two, 100), np.ones(100))
# y = x.copy().T
# z = function(x, y)
# fig.add_trace(go.Surface(x=x, y=y, z=z))
# fig.show()
# # print(x1, y1, z1)
#
# for a, b, c in zip(x, y, z):
#     print(a, 'x', b,'y', c, 'y')
'''
import math
import random
def function(x):
    return -(x - 2) ** 2
def fitness_particle(particle):
    best_p_position = -math.inf
    for x in particle:
        if function(x) > function(best_p_position):
            best_p_position = x
    return best_p_position

def fitnes_swarm(swarm):  # лучшая позиция точки
    best_s_position = -math.inf
    for particle in swarm:
        for x in particle:
            if function(x) > function(best_s_position):
                best_s_position = x
    return best_s_position


population = [[],[],[],[]]

for i in population:
    i.append(random.uniform(-5, 5))

# for i in population:
#     print(i, '\n')

# print(fitnes_swarm(population), 'g')


# for particle in population:
#     print(fitness_particle(particle), 'p')

velocity = random.uniform(-(5 - -5), 5 - -5)
print(velocity, 'start vel')

Omega = 0.5671432904097838729999686622
r_p, r_g = random.random(), random.random()
Phi_p = 1
Phi_g = 1
count = 0


temp = [[],[],[],[]]
count1 = 0

for i in population:
    velocity_up = Omega * velocity + (Phi_p * r_p * (fitness_particle(i) - i[count])) + (Phi_g * r_g * (fitnes_swarm(population) - i[count]))
    print(fitness_particle(i), 'fit particle')
    print(fitnes_swarm(population), 'fit swarm')
    print(velocity_up, 'second velocity')
    temp[count1].append(i[count] + velocity_up)
    count1 += 1



for i in population:
    print(i, '\n')

for i in temp:
    print(i)
    '''

import numpy as np
import random
import plotly.express as px
import math
import plotly.graph_objects as go
import copy

num_particles = int(input('Количество точек '))
population_fitted = []
population = []
part_cord_array = []
lim1 = int(input('Первый лимит '))
lim2 = int(input('Второй лимит '))
best_position = -math.inf
# best_swarm_position = -math.inf
iterations = int((input('Количество итераций ')))
Omega = 0.5671432904097838729999686622
Phi = 0.618
count = 0
# velocity = random.uniform(-(lim2 - lim1), lim2 - lim1)
velocity = 0

# > --------------------------------------------------------------------

def function(x):
    return -(x - 2) ** 2


for i in range(num_particles):
    population.append(part_cord_array)
    part_cord_array = []

temp_cords = []





def fitnes_swarm(swarm):  # лучшая позиция точки
    best_s_position = -math.inf
    for particle in swarm:
        for x in particle:
            if function(x) > function(best_s_position):
                best_s_position = x
                # print(best_position)
    return best_s_position


def fitness_particle(particle):
    best_p_position = -math.inf
    for x in particle:
        if function(x) > function(best_p_position):
            best_p_position = x
    return best_p_position


# > --------------------------------------------------------------------
# начальная позиция точек
for i in population:
    i.append(random.uniform(lim1, lim2))
velocity = random.uniform(-(lim2 - lim1), lim2 - lim1)




# > --------------------------------------------------------------------
for i in range(iterations):
    Phi_p = 1
    Phi_g = 1
    for i in range(len(population)):
        velocity_up = Omega * velocity + (Phi_p * random.random() * (fitness_particle(population[i]) - population[i][count])) + (Phi_g * random.random() * (fitnes_swarm(population) - population[i][count]))
        temp_cords.append(population[i][count] + velocity_up)
        velocity = velocity_up
        population[i].append(temp_cords[i])

    temp_cords = []
    print(temp_cords)
    count += 1
    print(count, 'c')

temp = []
for i in population:
    for g in i:
        temp.append(function(g))
    population_fitted.append(temp)
    temp = []

# > --------------------------------------------------------------------

x = []
y = []

for i in population:
    x.append(fitness_particle(i))
    y.append(function(fitness_particle(i)))

fig = px.scatter(x=x, y=y)
x_one = np.linspace(lim1, lim2, 100)
y_one = []
for i in x_one:
    y_one.append(function(i))

# for a, b in zip(x, y):
#     print(a, b, '\n')

fig.add_trace(go.Scatter(x=x_one, y=y_one))
fig.show()

# for i in population:
#     print(i, '\n')


# print(fitnes_swarm(population),'fit swarm')
# for i in population:
#     print(fitness_particle(i), 'fit part')


# print(best_position, function(best_position), velocity)
