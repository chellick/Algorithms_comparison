# # # # import numpy as np
# # # # import matplotlib.pyplot as plt
# # # # def fun(x):
# # # #     return -x**2
# # # # fig = plt.figure()
# # # # a = [i for i in range(100)]
# # # # b = [fun(a[i]) for i in range(100)]
# # # # x = a
# # # # y = b
# # # # for i in range(100):
# # # #     plt.scatter(x[i], y[i])
# # # # #plt.plot(x, y)
# # # #
# # # #
# # # # plt.show()
# # #
# # # # from calendar import c
# # # # from os import sep
# # # from random import randint, random
# # # # import numpy as np
# # # import matplotlib.pyplot as plt
# # # fitness = []
# # # temp_count_fit = 0
# # # child = []
# # # count = 0
# # # count2 = 0
# # # best = 0
# # # space = ""
# # # parent_one = []
# # # parent_two = []
# # # population = []
# # # countc = 0
# # # count_str = []
# # # individ = int(input("сколько хотите индивидов?  "))
# # # len_individ = int(input("длина индивидов  "))
# # # steps = int(input("кол-во поколений  "))
# # # sep_population = []
# # # count_str_x = []
# # # best_p = []
# # # best_count = 0
# # # best_temp = 0
# # #
# # # for i in range(individ):
# # #     num_child = []
# # #     for i in range(len_individ):
# # #         a = randint(0, 1)
# # #         num_child.append(a)
# # #     population.append(num_child)
# # # print(population, "первая")
# # #
# # # for i in population:
# # #     for i in population:
# # #         if best <= sum(i):
# # #             best = sum(i)
# # #         temp_count_fit += sum(i)
# # #
# # #     # count_pr = temp_count_fit / individ
# # # best_p.append(best)
# # # count_str.append(temp_count_fit / individ)
# # #
# # # for i in range((steps - 1) * individ):  # Основной цикл создания популяций
# # #     #  while countc < len_individ:
# # #     fp = population[randint(0, len(population) - 1)]  # Турнирный метод отбора родителей
# # #     sp = population[randint(0, len(population) - 1)]
# # #
# # #
# # #
# # #     if sum(fp) >= sum(sp):
# # #         parent_one = fp
# # #     else:
# # #         parent_one = sp
# # #
# # #     fp = population[randint(0, len(population) - 1)]  # Турнирный метод отбора родителей
# # #     sp = population[randint(0, len(population) - 1)]
# # #
# # #     if sum(fp) >= sum(sp):
# # #         parent_one = fp
# # #     else:
# # #         parent_one = sp
# # #
# # #
# # #     rand = randint(0, len_individ - 1)  # Метод выборки ребенка путем скрещивания частей генотипа родителей
# # #     fh = parent_one[:rand]  # first half
# # #     sh = parent_two[rand::]  # second half
# # #     child = fh + sh
# # #
# # #     for i in range(len(child)):  # Метод мутации
# # #         rand = random()
# # #         if rand <= 0.02:
# # #             child[i] = 1 if child[i] == 0 else 0
# # #     """
# # #     for i in child:  #  Нахождение количества едениц в генотипе ребёнка
# # #         if i == 1:
# # #             countc += 1
# # #     count_str.append(countc)
# # #     countc = 0
# # #
# # #     #  print(countc, d)
# # #
# # #     #  print(child, "child")
# # #     """
# # #     sep_population.append(child)  # Добавление ребенка в список
# # #     #  print(sep_population, "changed population")
# # #     #  print(population, " популяция ", sep_population, " дочерняя популяция ")
# # #
# # #     if len(population) == len(sep_population):
# # #         for i in population:
# # #             if best <= sum(i):
# # #                 best = sum(i)
# # #             temp_count_fit += sum(i)
# # #
# # #         # count_pr = temp_count_fit / individ
# # #         best_p.append(best)
# # #         count_str.append(temp_count_fit / individ)
# # #
# # #         # count_str_x.append(num_generation)
# # #         population = sep_population.copy()
# # #         sep_population = []
# # #
# # #     temp_count_fit = 0
# # #     #  print(population, "популяция")
# # #
# # # for ex in range(len(count_str) + 1):
# # #     count_str_x = list(range(1, ex + 1))
# # # #  print(count_str_x, "len str x")
# # # #  print(count_str, "пригодность")
# # # print(child)
# # #
# # # for ex in range(len(best_p) + 1):
# # #     best_p_x = list(range(1, ex + 1))
# # # # print(population)
# # # # print(best_p, best_p_x, "best_count")
# # # print(count_str, 'count str ')  # , count_str_x)
# # # # print(num_generation, "num_generation")
# # #
# # #
# # # figure, axis = plt.subplots()
# # #
# # # x = count_str_x
# # # y = count_str
# # # x1 = best_p_x
# # # y1 = best_p
# # # print(best_p, best_p_x)
# # # axis.plot(x, y, linewidth=2.0)
# # # axis.plot(x1, y1)
# # # axis.set(xlim=(0, len(best_p_x) + 1))
# # #
# # # plt.show()
# #
# # # from calendar import c
# # # from os import sep
# # # from random import randint, random
# # import numpy as np
# # import matplotlib.pyplot as plt
# #
# # from random import randint, random
# # import numpy as np
# # import matplotlib.pyplot as plt
# #
# # temp_count_fit = 0
# # child = []
# # count = 0
# # count2 = 0
# # best = 0
# # space = ""
# # parent_one = []
# # parent_two = []
# # population = []
# # countc = 0
# # count_str = []
# # individ = int(input("сколько хотите индивидов?  "))
# # len_individ = int(input("длина индивидов  "))
# # steps = int(input("кол-во поколений  "))
# # sep_population = []
# # count_str_x = []
# # best_p = []
# # best_count = 0
# #
# #
# # # >--------------------------------------------------------------------------------------------------------
# #
# # def fitness(individ):
# #     return sum(individ)
# #
# #
# # for i in range(individ):
# #     num_child = []
# #     for i in range(len_individ):
# #         a = randint(0, 1)
# #         num_child.append(a)
# #     population.append(num_child)
# # print(population, "первая")
# #
# #
# # for i in population:
# #     if best <= fitness(i):
# #         best = fitness(i)
# #     temp_count_fit += fitness(i)
# # count_str.append(temp_count_fit / individ)
# # best_p.append(best)
# #
# # for i in range((steps - 1) * individ):  # Основной цикл создания популяций
# #     #  while countc < len_individ:
# # # >--------------------------------------------------------------------------------------------------------
# #     fp = population[randint(0, len(population) - 1)]  # Турнирный метод отбора родителей
# #     sp = population[randint(0, len(population) - 1)]
# #
# #     if fitness(fp) >= fitness(sp):
# #         parent_one = fp
# #     else:
# #         parent_one = sp
# #
# #     fp = population[randint(0, len(population) - 1)]  # выборка индивидов из массива population
# #     sp = population[randint(0, len(population) - 1)]
# #
# #     if fitness(fp) >= fitness(sp):
# #         parent_two = fp
# #     else:
# #         parent_two = sp
# #
# #     fp = population[randint(0, len(population) - 1)]  # выборка индивидов из массива population
# #     sp = population[randint(0, len(population) - 1)]
# # # >--------------------------------------------------------------------------------------------------------
# #     rand = randint(0, len_individ - 1)  # Метод выборки ребенка путем скрещивания частей генотипа родителей
# #     fh = parent_one[:rand]  # first half
# #     sh = parent_two[rand::]  # second half
# #     child = fh + sh
# #
# #     for i in range(len(child)):  # Метод мутации
# #         rand = random()
# #         if rand <= 0.02:
# #             child[i] = 1 if child[i] == 0 else 0
# #     """
# #     for i in child:  #  Нахождение количества едениц в генотипе ребёнка
# #         if i == 1:
# #             countc += 1
# #     count_str.append(countc)
# #     countc = 0
# #
# #     #  print(countc, d)
# #
# #     #  print(child, "child")
# #     """
# #     sep_population.append(child)  # Добавление ребенка в список
# #     #  print(sep_population, "changed population")
# #     #  print(population, " популяция ", sep_population, " дочерняя популяция ")
# # # >--------------------------------------------------------------------------------------------------------
# #     if len(population) == len(sep_population):
# #         for i in population:
# #             if best <= fitness(i):
# #                 best = fitness(i)
# #             temp_count_fit += fitness(i)
# #
# #         # count_pr = temp_count_fit / individ
# #         best_p.append(best)
# #         count_str.append(temp_count_fit / individ)
# #
# #         # count_str_x.append(num_generation)
# #         population = sep_population.copy()
# #         sep_population = []
# #
# #     temp_count_fit = 0
# #     #  print(population, "популяция")
# # # >--------------------------------------------------------------------------------------------------------
# #
# # for ex in range(len(count_str) + 1):
# #     count_str_x = list(range(1, ex + 1))
# # #  print(count_str_x, "len str x")
# # #  print(count_str, "пригодность")
# # print(child)
# #
# # for ex in range(len(best_p) + 1):
# #     best_p_x = list(range(1, ex + 1))
# # # print(population)
# # # print(best_p, best_p_x, "best_count")
# # print(count_str, 'count str ')  # , count_str_x)
# # # print(num_generation, "num_generation")
# # # >--------------------------------------------------------------------------------------------------------
# #
# # figure, axis = plt.subplots()
# #
# # x = count_str_x
# # y = count_str
# # x1 = best_p_x
# # y1 = best_p
# # print(best_p, best_p_x)
# # axis.plot(x, y, linewidth=2.0)
# # axis.plot(x1, y1)
# # axis.set(xlim=(0, len(best_p_x) + 1))
# #
# # plt.show()
#
# # from calendar import c
# # from os import sep
#
# from random import randint, random
# import numpy as np
# import matplotlib.pyplot as plt
#
# temp_count_fit = 0
# child = []
# count = 0
# count2 = 0
# best = 0
# space = ""
# parent_one = []
# parent_two = []
# population = []
# countc = 0
# count_str = []
# individ = int(input("сколько хотите индивидов?  "))
# len_individ = int(input("длина индивидов  "))
# steps = int(input("кол-во поколений  "))
# sep_population = []
# count_str_x = []
# best_p = []
# best_count = 0
# population_fit = []
# lst_fit_temp = []
#
# # >--------------------------------------------------------------------------------------------------------
#
# def fitness(individ):
#     return sum(individ)
#
#
# for i in range(individ):
#     num_child = []
#     for i in range(len_individ):
#         a = randint(0, 1)
#         num_child.append(a)
#     population.append(num_child)
# print(population, "первая")
# for i in population:
#     population_fit.append(fitness(i))
#
#
#
# for i in population_fit:
#     if best <= i:
#         best = i
#     temp_count_fit += i
# count_str.append(temp_count_fit / individ)
# best_p.append(best)
#
# for i in range((steps - 1) * individ):  # Основной цикл создания популяций
#     #  while countc < len_individ:
# # >--------------------------------------------------------------------------------------------------------
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
#     # fp = population[randint(0, len(population) - 1)]  # выборка индивидов из массива population
#     # sp = population[randint(0, len(population) - 1)]
# # >--------------------------------------------------------------------------------------------------------
#     rand = randint(0, len_individ - 1)  # Метод выборки ребенка путем скрещивания частей генотипа родителей
#     fh = parent_one[:rand]  # first half
#     sh = parent_two[rand::]  # second half
#     child = fh + sh
#
#     for i in range(len(child)):  # Метод мутации
#         rand = random()
#         if rand <= 0.02:
#             child[i] = 1 if child[i] == 0 else 0
#     lst_fit_temp.append(fitness(child))
#     sep_population.append(child)  # Добавление ребенка в список
#
#  # >--------------------------------------------------------------------------------------------------------
#     if len(population) == len(sep_population):
#         for i in population_fit:
#             if best <= i:
#                 best = i
#             temp_count_fit += i
#
#         best_p.append(best)
#         count_str.append(temp_count_fit / individ)
#
#         population_fit = lst_fit_temp.copy()
#         population = sep_population.copy()
#         sep_population = []
#         lst_fit_temp = []
#
#     temp_count_fit = 0
#     #  print(population, "популяция")
# # >--------------------------------------------------------------------------------------------------------
#
# for ex in range(len(count_str) + 1):
#     count_str_x = list(range(1, ex + 1))
# #  print(count_str_x, "len str x")
# #  print(count_str, "пригодность")
# print(child)
#
# for ex in range(len(best_p) + 1):
#     best_p_x = list(range(1, ex + 1))
# # print(population)
# # print(best_p, best_p_x, "best_count")
# print(count_str, 'count str ')  # , count_str_x)
# # print(num_generation, "num_generation")
# # >--------------------------------------------------------------------------------------------------------
#
# figure, axis = plt.subplots()
# x = count_str_x
# y = count_str
# x1 = best_p_x
# y1 = best_p
# print(best_p, best_p_x)
# axis.plot(x, y, linewidth=2.0)
# axis.plot(x1, y1)
# axis.set(xlim=(0, len(best_p_x) + 1))
#
# plt.show()
#
import math
from random import randint, random
import numpy as np
import matplotlib.pyplot as plt
import math

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
mutation_veriety = float(input("вероятность мутации   "))
sep_population = []
count_str_x = []
best_p = []
best_count = 0
lst_fit = []
lst_fit_x = []
lst_fit_temp = []
best_individ = []
limit1 = int(input("ограничение 1 "))
limit2= int(input("ограничение 2 "))
best = -math.inf

# >--------------------------------------------------------------------------------------------------------

def fitness(individ):
    s_individ = "".join(map(str, individ))
    int_individ = int(s_individ, 2)
    float_individ = (int_individ / (2 ** len(individ) * (limit2 - limit1) + limit1))
    float_individ_y = -(float_individ ** 2)
    return float_individ_y

def fitness_x(individ):
    s_individ = "".join(map(str, individ))
    int_individ = int(s_individ, 2)
    float_individ = (int_individ / (2 ** len(individ) * (limit2 - limit1) + limit1))
    return float_individ
# >--------------------------------------------------------------------------------------------------------

for i in range(indiv):
    c1 = []
    for i in range(dlin):
        a = randint(0, 1)
        c1.append(a)
    population.append(c1)


for i in population:
    lst_fit.append(fitness_x(i))

for i in lst_fit:
    if best <= i:
        best = i
    temp_count_pr += i

count_str.append(temp_count_pr / indiv)
best_p.append(best)

# >--------------------------------------------------------------------------------------------------------
for i in range((steps - 1) * indiv):  # Основной цикл создания популяций
    #  while countc < len_individ:
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
        if rand <= mutation_veriety:
            child[i] = 1 if child[i] == 0 else 0
    lst_fit_temp.append(fitness_x(child))
    sep_population.append(child)  # Добавление ребенка в список

# >--------------------------------------------------------------------------------------------------------
    if len(population) == len(sep_population):
        for i in lst_fit_temp:
            if best <= i:
                best = i
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


best_individ = best_individ[::-1]
del best_individ[1:]

# >--------------------------------------------------------------------------------------------------------
print(count_str, 'count str ')
print(best_individ, 'best individ')
print(child, 'child')

# >--------------------------------------------------------------------------------------------------------
figure, axis = plt.subplots()
x_one = np.linspace(-100, 100, 1000)
y_one = [-(i**2) for i in x_one]
x = best_p
y = [-(i**2) for i in best_p]

plt.scatter(x, y, 20)
axis.plot(x_one, y_one)
plt.show()
print(best_p , 'x')
print(y, 'y')
# >--------------------------------------------------------------------------------------------------------
# figure, axis = plt.subplots()
# x = count_str_x
# y = count_str
# x1 = best_p_x
# y1 = best_p
# print(best_p, best_p_x)
# axis.plot(x, y, linewidth=2.0)
# axis.plot(x1, y1)
# # axis.set(xlim=(0, len(best_p_x) + 1))
#
# plt.show()
