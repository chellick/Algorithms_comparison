# # # # # # import numpy as np
# # # # # # import matplotlib.pyplot as plt
# # # # # # def fun(x):
# # # # # #     return -x**2
# # # # # # fig = plt.figure()
# # # # # # a = [i for i in range(100)]
# # # # # # b = [fun(a[i]) for i in range(100)]
# # # # # # x = a
# # # # # # y = b
# # # # # # for i in range(100):
# # # # # #     plt.scatter(x[i], y[i])
# # # # # # #plt.plot(x, y)
# # # # # #
# # # # # #
# # # # # # plt.show()
# # # # #
# # # # # # from calendar import c
# # # # # # from os import sep
# # # # # from random import randint, random
# # # # # # import numpy as np
# # # # # import matplotlib.pyplot as plt
# # # # # fitness = []
# # # # # temp_count_fit_y = 0
# # # # # child = []
# # # # # count = 0
# # # # # count2 = 0
# # # # # best_y = 0
# # # # # space = ""
# # # # # parent_one = []
# # # # # parent_two = []
# # # # # population = []
# # # # # countc = 0
# # # # # count_str_y = []
# # # # # count_individ = int(input("сколько хотите индивидов?  "))
# # # # # len_individ = int(input("длина индивидов  "))
# # # # # count_generations = int(input("кол-во поколений  "))
# # # # # child_population = []
# # # # # count_str_x = []
# # # # # best_individ_array_y = []
# # # # # best_count = 0
# # # # # best_temp = 0
# # # # #
# # # # # for i in range(count_individ):
# # # # #     num_individ = []
# # # # #     for i in range(len_individ):
# # # # #         a = randint(0, 1)
# # # # #         num_individ.append(a)
# # # # #     population.append(num_individ)
# # # # # print(population, "первая")
# # # # #
# # # # # for i in population:
# # # # #     for i in population:
# # # # #         if best_y <= sum(i):
# # # # #             best_y = sum(i)
# # # # #         temp_count_fit_y += sum(i)
# # # # #
# # # # #     # count_pr = temp_count_fit_y / count_individ
# # # # # best_individ_array_y.append(best_y)
# # # # # count_str_y.append(temp_count_fit_y / count_individ)
# # # # #
# # # # # for i in range((count_generations - 1) * count_individ):  # Основной цикл создания популяций
# # # # #     #  while countc < len_individ:
# # # # #     fp = population[randint(0, len(population) - 1)]  # Турнирный метод отбора родителей
# # # # #     sp = population[randint(0, len(population) - 1)]
# # # # #
# # # # #
# # # # #
# # # # #     if sum(fp) >= sum(sp):
# # # # #         parent_one = fp
# # # # #     else:
# # # # #         parent_one = sp
# # # # #
# # # # #     fp = population[randint(0, len(population) - 1)]  # Турнирный метод отбора родителей
# # # # #     sp = population[randint(0, len(population) - 1)]
# # # # #
# # # # #     if sum(fp) >= sum(sp):
# # # # #         parent_one = fp
# # # # #     else:
# # # # #         parent_one = sp
# # # # #
# # # # #
# # # # #     rand = randint(0, len_individ - 1)  # Метод выборки ребенка путем скрещивания частей генотипа родителей
# # # # #     fh = parent_one[:rand]  # first half
# # # # #     sh = parent_two[rand::]  # second half
# # # # #     child = fh + sh
# # # # #
# # # # #     for i in range(len(child)):  # Метод мутации
# # # # #         rand = random()
# # # # #         if rand <= 0.02:
# # # # #             child[i] = 1 if child[i] == 0 else 0
# # # # #     """
# # # # #     for i in child:  #  Нахождение количества едениц в генотипе ребёнка
# # # # #         if i == 1:
# # # # #             countc += 1
# # # # #     count_str_y.append(countc)
# # # # #     countc = 0
# # # # #
# # # # #     #  print(countc, d)
# # # # #
# # # # #     #  print(child, "child")
# # # # #     """
# # # # #     child_population.append(child)  # Добавление ребенка в список
# # # # #     #  print(child_population, "changed population")
# # # # #     #  print(population, " популяция ", child_population, " дочерняя популяция ")
# # # # #
# # # # #     if len(population) == len(child_population):
# # # # #         for i in population:
# # # # #             if best_y <= sum(i):
# # # # #                 best_y = sum(i)
# # # # #             temp_count_fit_y += sum(i)
# # # # #
# # # # #         # count_pr = temp_count_fit_y / count_individ
# # # # #         best_individ_array_y.append(best_y)
# # # # #         count_str_y.append(temp_count_fit_y / count_individ)
# # # # #
# # # # #         # count_str_x.append(num_generation)
# # # # #         population = child_population.copy()
# # # # #         child_population = []
# # # # #
# # # # #     temp_count_fit_y = 0
# # # # #     #  print(population, "популяция")
# # # # #
# # # # # for ex in range(len(count_str_y) + 1):
# # # # #     count_str_x = list(range(1, ex + 1))
# # # # # #  print(count_str_x, "len str x")
# # # # # #  print(count_str_y, "пригодность")
# # # # # print(child)
# # # # #
# # # # # for ex in range(len(best_individ_array_y) + 1):
# # # # #     best_p_x = list(range(1, ex + 1))
# # # # # # print(population)
# # # # # # print(best_individ_array_y, best_p_x, "best_count")
# # # # # print(count_str_y, 'count str ')  # , count_str_x)
# # # # # # print(num_generation, "num_generation")
# # # # #
# # # # #
# # # # # figure, axis = plt.subplots()
# # # # #
# # # # # x = count_str_x
# # # # # y = count_str_y
# # # # # x1 = best_p_x
# # # # # y1 = best_individ_array_y
# # # # # print(best_individ_array_y, best_p_x)
# # # # # axis.plot(x, y, linewidth=2.0)
# # # # # axis.plot(x1, y1)
# # # # # axis.set(xlim=(0, len(best_p_x) + 1))
# # # # #
# # # # # plt.show()
# # # #
# # # # # from calendar import c
# # # # # from os import sep
# # # # # from random import randint, random
# # # # import numpy as np
# # # # import matplotlib.pyplot as plt
# # # #
# # # # from random import randint, random
# # # # import numpy as np
# # # # import matplotlib.pyplot as plt
# # # #
# # # # temp_count_fit_y = 0
# # # # child = []
# # # # count = 0
# # # # count2 = 0
# # # # best_y = 0
# # # # space = ""
# # # # parent_one = []
# # # # parent_two = []
# # # # population = []
# # # # countc = 0
# # # # count_str_y = []
# # # # count_individ = int(input("сколько хотите индивидов?  "))
# # # # len_individ = int(input("длина индивидов  "))
# # # # count_generations = int(input("кол-во поколений  "))
# # # # child_population = []
# # # # count_str_x = []
# # # # best_individ_array_y = []
# # # # best_count = 0
# # # #
# # # #
# # # # # >--------------------------------------------------------------------------------------------------------
# # # #
# # # # def fitness(count_individ):
# # # #     return sum(count_individ)
# # # #
# # # #
# # # # for i in range(count_individ):
# # # #     num_individ = []
# # # #     for i in range(len_individ):
# # # #         a = randint(0, 1)
# # # #         num_individ.append(a)
# # # #     population.append(num_individ)
# # # # print(population, "первая")
# # # #
# # # #
# # # # for i in population:
# # # #     if best_y <= fitness(i):
# # # #         best_y = fitness(i)
# # # #     temp_count_fit_y += fitness(i)
# # # # count_str_y.append(temp_count_fit_y / count_individ)
# # # # best_individ_array_y.append(best_y)
# # # #
# # # # for i in range((count_generations - 1) * count_individ):  # Основной цикл создания популяций
# # # #     #  while countc < len_individ:
# # # # # >--------------------------------------------------------------------------------------------------------
# # # #     fp = population[randint(0, len(population) - 1)]  # Турнирный метод отбора родителей
# # # #     sp = population[randint(0, len(population) - 1)]
# # # #
# # # #     if fitness(fp) >= fitness(sp):
# # # #         parent_one = fp
# # # #     else:
# # # #         parent_one = sp
# # # #
# # # #     fp = population[randint(0, len(population) - 1)]  # выборка индивидов из массива population
# # # #     sp = population[randint(0, len(population) - 1)]
# # # #
# # # #     if fitness(fp) >= fitness(sp):
# # # #         parent_two = fp
# # # #     else:
# # # #         parent_two = sp
# # # #
# # # #     fp = population[randint(0, len(population) - 1)]  # выборка индивидов из массива population
# # # #     sp = population[randint(0, len(population) - 1)]
# # # # # >--------------------------------------------------------------------------------------------------------
# # # #     rand = randint(0, len_individ - 1)  # Метод выборки ребенка путем скрещивания частей генотипа родителей
# # # #     fh = parent_one[:rand]  # first half
# # # #     sh = parent_two[rand::]  # second half
# # # #     child = fh + sh
# # # #
# # # #     for i in range(len(child)):  # Метод мутации
# # # #         rand = random()
# # # #         if rand <= 0.02:
# # # #             child[i] = 1 if child[i] == 0 else 0
# # # #     """
# # # #     for i in child:  #  Нахождение количества едениц в генотипе ребёнка
# # # #         if i == 1:
# # # #             countc += 1
# # # #     count_str_y.append(countc)
# # # #     countc = 0
# # # #
# # # #     #  print(countc, d)
# # # #
# # # #     #  print(child, "child")
# # # #     """
# # # #     child_population.append(child)  # Добавление ребенка в список
# # # #     #  print(child_population, "changed population")
# # # #     #  print(population, " популяция ", child_population, " дочерняя популяция ")
# # # # # >--------------------------------------------------------------------------------------------------------
# # # #     if len(population) == len(child_population):
# # # #         for i in population:
# # # #             if best_y <= fitness(i):
# # # #                 best_y = fitness(i)
# # # #             temp_count_fit_y += fitness(i)
# # # #
# # # #         # count_pr = temp_count_fit_y / count_individ
# # # #         best_individ_array_y.append(best_y)
# # # #         count_str_y.append(temp_count_fit_y / count_individ)
# # # #
# # # #         # count_str_x.append(num_generation)
# # # #         population = child_population.copy()
# # # #         child_population = []
# # # #
# # # #     temp_count_fit_y = 0
# # # #     #  print(population, "популяция")
# # # # # >--------------------------------------------------------------------------------------------------------
# # # #
# # # # for ex in range(len(count_str_y) + 1):
# # # #     count_str_x = list(range(1, ex + 1))
# # # # #  print(count_str_x, "len str x")
# # # # #  print(count_str_y, "пригодность")
# # # # print(child)
# # # #
# # # # for ex in range(len(best_individ_array_y) + 1):
# # # #     best_p_x = list(range(1, ex + 1))
# # # # # print(population)
# # # # # print(best_individ_array_y, best_p_x, "best_count")
# # # # print(count_str_y, 'count str ')  # , count_str_x)
# # # # # print(num_generation, "num_generation")
# # # # # >--------------------------------------------------------------------------------------------------------
# # # #
# # # # figure, axis = plt.subplots()
# # # #
# # # # x = count_str_x
# # # # y = count_str_y
# # # # x1 = best_p_x
# # # # y1 = best_individ_array_y
# # # # print(best_individ_array_y, best_p_x)
# # # # axis.plot(x, y, linewidth=2.0)
# # # # axis.plot(x1, y1)
# # # # axis.set(xlim=(0, len(best_p_x) + 1))
# # # #
# # # # plt.show()
# # #
# # # # from calendar import c
# # # # from os import sep
# # #
# # # from random import randint, random
# # # import numpy as np
# # # import matplotlib.pyplot as plt
# # #
# # # temp_count_fit_y = 0
# # # child = []
# # # count = 0
# # # count2 = 0
# # # best_y = 0
# # # space = ""
# # # parent_one = []
# # # parent_two = []
# # # population = []
# # # countc = 0
# # # count_str_y = []
# # # count_individ = int(input("сколько хотите индивидов?  "))
# # # len_individ = int(input("длина индивидов  "))
# # # count_generations = int(input("кол-во поколений  "))
# # # child_population = []
# # # count_str_x = []
# # # best_individ_array_y = []
# # # best_count = 0
# # # population_fit_y = []
# # # lst_fit_temp_y = []
# # #
# # # # >--------------------------------------------------------------------------------------------------------
# # #
# # # def fitness(count_individ):
# # #     return sum(count_individ)
# # #
# # #
# # # for i in range(count_individ):
# # #     num_individ = []
# # #     for i in range(len_individ):
# # #         a = randint(0, 1)
# # #         num_individ.append(a)
# # #     population.append(num_individ)
# # # print(population, "первая")
# # # for i in population:
# # #     population_fit_y.append(fitness(i))
# # #
# # #
# # #
# # # for i in population_fit_y:
# # #     if best_y <= i:
# # #         best_y = i
# # #     temp_count_fit_y += i
# # # count_str_y.append(temp_count_fit_y / count_individ)
# # # best_individ_array_y.append(best_y)
# # #
# # # for i in range((count_generations - 1) * count_individ):  # Основной цикл создания популяций
# # #     #  while countc < len_individ:
# # # # >--------------------------------------------------------------------------------------------------------
# # #     fp = randint(0, len(population) - 1)  # Турнирный метод отбора родителей
# # #     sp = randint(0, len(population) - 1)
# # #
# # #     if population_fit_y[fp] >= population_fit_y[sp]:
# # #         parent_one = population[fp]
# # #     else:
# # #         parent_one = population[sp]
# # #
# # #     fp = randint(0, len(population) - 1)  # Турнирный метод отбора родителей
# # #     sp = randint(0, len(population) - 1)
# # #
# # #     if population_fit_y[fp] >= population_fit_y[sp]:
# # #         parent_two = population[fp]
# # #     else:
# # #         parent_two = population[sp]
# # #
# # #     # fp = population[randint(0, len(population) - 1)]  # выборка индивидов из массива population
# # #     # sp = population[randint(0, len(population) - 1)]
# # # # >--------------------------------------------------------------------------------------------------------
# # #     rand = randint(0, len_individ - 1)  # Метод выборки ребенка путем скрещивания частей генотипа родителей
# # #     fh = parent_one[:rand]  # first half
# # #     sh = parent_two[rand::]  # second half
# # #     child = fh + sh
# # #
# # #     for i in range(len(child)):  # Метод мутации
# # #         rand = random()
# # #         if rand <= 0.02:
# # #             child[i] = 1 if child[i] == 0 else 0
# # #     lst_fit_temp_y.append(fitness(child))
# # #     child_population.append(child)  # Добавление ребенка в список
# # #
# # #  # >--------------------------------------------------------------------------------------------------------
# # #     if len(population) == len(child_population):
# # #         for i in population_fit_y:
# # #             if best_y <= i:
# # #                 best_y = i
# # #             temp_count_fit_y += i
# # #
# # #         best_individ_array_y.append(best_y)
# # #         count_str_y.append(temp_count_fit_y / count_individ)
# # #
# # #         population_fit_y = lst_fit_temp_y.copy()
# # #         population = child_population.copy()
# # #         child_population = []
# # #         lst_fit_temp_y = []
# # #
# # #     temp_count_fit_y = 0
# # #     #  print(population, "популяция")
# # # # >--------------------------------------------------------------------------------------------------------
# # #
# # # for ex in range(len(count_str_y) + 1):
# # #     count_str_x = list(range(1, ex + 1))
# # # #  print(count_str_x, "len str x")
# # # #  print(count_str_y, "пригодность")
# # # print(child)
# # #
# # # for ex in range(len(best_individ_array_y) + 1):
# # #     best_p_x = list(range(1, ex + 1))
# # # # print(population)
# # # # print(best_individ_array_y, best_p_x, "best_count")
# # # print(count_str_y, 'count str ')  # , count_str_x)
# # # # print(num_generation, "num_generation")
# # # # >--------------------------------------------------------------------------------------------------------
# # #
# # # figure, axis = plt.subplots()
# # # x = count_str_x
# # # y = count_str_y
# # # x1 = best_p_x
# # # y1 = best_individ_array_y
# # # print(best_individ_array_y, best_p_x)
# # # axis.plot(x, y, linewidth=2.0)
# # # axis.plot(x1, y1)
# # # axis.set(xlim=(0, len(best_p_x) + 1))
# # #
# # # plt.show()
# # #
# # import math
# # from random import randint, random
# # import numpy as np
# # import matplotlib.pyplot as plt
# # import math
# #
# # temp_count_pr = 0
# # child = []
# # count = 0
# # count2 = 0
# # best_y = 0
# # space = ""
# # parent1 = []
# # parent2 = []
# # population = []
# # countc = 0
# # count_str_y = []
# # indiv = int(input("сколько хотите индивидов?  "))
# # dlin = int(input("длина индивидов  "))
# # steps = int(input("кол-во поколений  "))
# # mutation_veriety = float(input("вероятность мутации   "))
# # sep_population = []
# # count_str_x = []
# # best_p = []
# # best_count = 0
# # lst_fit = []
# # lst_fit_x = []
# # lst_fit_temp_y = []
# # best_individ_y = []
# # limit1 = int(input("ограничение 1 "))
# # limit2= int(input("ограничение 2 "))
# # best_y = -math.inf
# #
# # # >--------------------------------------------------------------------------------------------------------
# #
# # def fitness(individ):
# #     s_individ = "".join(map(str, individ))
# #     int_individ = int(s_individ, 2)
# #     float_individ = (int_individ / (2 ** len(individ) * (limit2 - limit1) + limit1))
# #     float_individ_y = -(float_individ ** 2)
# #     return float_individ_y
# #
# # def fitness_x(individ):
# #     s_individ = "".join(map(str, individ))
# #     int_individ = int(s_individ, 2)
# #     float_individ = (int_individ / (2 ** len(individ) * (limit2 - limit1) + limit1))
# #     return float_individ
# # # >--------------------------------------------------------------------------------------------------------
# #
# # for i in range(indiv):
# #     c1 = []
# #     for i in range(dlin):
# #         a = randint(0, 1)
# #         c1.append(a)
# #     population.append(c1)
# #
# #
# # for i in population:
# #     lst_fit.append(fitness_x(i))
# #
# # for i in lst_fit:
# #     if best_y <= i:
# #         best_y = i
# #     temp_count_pr += i
# #
# # count_str_y.append(temp_count_pr / indiv)
# # best_p.append(best_y)
# #
# # # >--------------------------------------------------------------------------------------------------------
# # for i in range((steps - 1) * indiv):  # Основной цикл создания популяций
# #     #  while countc < len_individ:
# # # >--------------------------------------------------------------------------------------------------------
# #     fp = randint(0, len(population) - 1)  # Турнирный метод отбора родителей
# #     sp = randint(0, len(population) - 1)
# #
# #     if lst_fit[fp] >= lst_fit[sp]:
# #         parent1 = population[fp]
# #     else:
# #         parent1 = population[sp]
# #
# #     fp = randint(0, len(population) - 1)  # Турнирный метод отбора родителей
# #     sp = randint(0, len(population) - 1)
# #
# #     if lst_fit[fp] >= lst_fit[sp]:
# #         parent2 = population[fp]
# #     else:
# #         parent2 = population[sp]
# #
# #     # fp = population[randint(0, len(population) - 1)]  # выборка индивидов из массива population
# #     # sp = population[randint(0, len(population) - 1)]
# # # >--------------------------------------------------------------------------------------------------------
# #     rand = randint(0, dlin - 1)  # Метод выборки ребенка путем скрещивания частей генотипа родителей
# #     fh = parent1[:rand]  # first half
# #     sh = parent2[rand::]  # second half
# #     child = fh + sh
# #
# #     for i in range(len(child)):  # Метод мутации
# #         rand = random()
# #         if rand <= mutation_veriety:
# #             child[i] = 1 if child[i] == 0 else 0
# #     lst_fit_temp_y.append(fitness_x(child))
# #     sep_population.append(child)  # Добавление ребенка в список
# #
# # # >--------------------------------------------------------------------------------------------------------
# #     if len(population) == len(sep_population):
# #         for i in lst_fit_temp_y:
# #             if best_y <= i:
# #                 best_y = i
# #             temp_count_pr += i
# #
# #         best_p.append(best_y)
# #         count_str_y.append(temp_count_pr / indiv)
# #
# #         lst_fit = lst_fit_temp_y.copy()
# #         population = sep_population.copy()
# #         sep_population = []
# #         lst_fit_temp_y = []
# #
# #     temp_count_pr = 0
# #     #  print(population, "популяция")
# #
# # # >--------------------------------------------------------------------------------------------------------
# #
# # for ex in range(len(count_str_y) + 1):
# #     count_str_x = list(range(1, ex + 1))
# #
# #
# # best_individ_y = best_individ_y[::-1]
# # del best_individ_y[1:]
# #
# # # >--------------------------------------------------------------------------------------------------------
# # print(count_str_y, 'count str ')
# # print(best_individ_y, 'best_y count_individ')
# # print(child, 'child')
# #
# # # >--------------------------------------------------------------------------------------------------------
# # figure, axis = plt.subplots()
# # x_one = np.linspace(-100, 100, 1000)
# # y_one = [-(i**2) for i in x_one]
# # x = best_p
# # y = [-(i**2) for i in best_p]
# #
# # plt.scatter(x, y, 20)
# # axis.plot(x_one, y_one)
# # plt.show()
# # print(best_p , 'x')
# # print(y, 'y')
# # # >--------------------------------------------------------------------------------------------------------
# # # figure, axis = plt.subplots()
# # # x = count_str_x
# # # y = count_str_y
# # # x1 = best_p_x
# # # y1 = best_individ_array_y
# # # print(best_individ_array_y, best_p_x)
# # # axis.plot(x, y, linewidth=2.0)
# # # axis.plot(x1, y1)
# # # # axis.set(xlim=(0, len(best_p_x) + 1))
# # #
# # # plt.show()
#
# # from calendar import c
# # from os import sep
#
#
# import math
# from random import randint, random
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d.art3d import Poly3DCollection
#
# temp_count_fit_z = 0
# temp_count_fit_y = 0
# child = []
# best_y = 0
# parent_one = []
# parent_two = []
# population = []
# count_str_y = []
# count_str_z = []
#
# child_population = []
# count_str_x = []
# best_individ_array_y = []
# best_individ_array_z = []
# population_fit_y = []
# population_fit_z = []
# lst_fit_x = []
# lst_fit_temp_y = []
# lst_fit_temp_z = []
# best_individ_y = []
# best_individ_x_one = []
# best_individ_z = []
# best_y = -math.inf
# best_z = -math.inf
#
#
# count_individ = int(input("сколько хотите индивидов?  "))
# len_individ = int(input("длина индивидов  "))
# count_generations = int(input("кол-во поколений  "))
# mutation_probability = float(input("вероятность мутации   "))
#
# limit_one = int(input("ограничение 1 "))
# limit_two = int(input("ограничение 2 "))
#
#
#
#
# # >--------------------------------------------------------------------------------------------------------
# def function(x):
#      return ((x** 2 + x - 11) ** 2 + (x + x ** 2 - 7) ** 2) * (-1)
# # def function(x):
# #     return -(x-2)**2
#
# def fitness_one(indiv):
#     s_individ = "".join(map(str, indiv))
#     int_individ = int(s_individ, 2)
#     float_individ = (int_individ / (2 ** len(indiv) - 1)) * (limit_two - limit_one) + limit_one
#     float_individ_y = function(float_individ)
#     return float_individ_y
#
# def fitness_two(indiv):
#     s_individ = "".join(map(str, indiv))
#     int_individ = int(s_individ, 2)
#     float_individ = (int_individ / (2 ** len(indiv) - 1)) * (limit_two - limit_one) + limit_one
#     float_individ_z = function(float_individ)
#     return float_individ_z
#
# def float_number(indiv):
#     s_indiv = "".join(map(str, indiv))
#     int_individ = int(s_indiv, 2)
#     float_individ = (int_individ / (2 ** len(indiv) - 1)) * (limit_two - limit_one) + limit_one
#     return float_individ
# # >--------------------------------------------------------------------------------------------------------
#
# for i in range(count_individ):
#     num_individ = []
#     for i in range(len_individ):
#         a = randint(0, 1)
#         num_individ.append(a)
#     population.append(num_individ)
#
#
#
# for i in population:
#     population_fit_y.append(fitness_one(i[:len(i) // 2]))
#
# for i in population:
#     population_fit_z.append(fitness_two(i[len(i) // 2:]))
#
#
#
# for i in range(len(population_fit_y)):
#     if best_y <= population_fit_y[i]:
#         best_y = population_fit_y[i]
#         index_y = i
#     temp_count_fit_y += population_fit_y[i]
#
# for i in range(len(population_fit_z)):
#     if best_z <= population_fit_z[i]:
#         best_z = population_fit_z[i]
#         index_z = i
#     temp_count_fit_z += population_fit_z[i]
#
#
#
#
# best_individ_y.append(population[index_y][:len_individ // 2])
# count_str_y.append(temp_count_fit_y / count_individ)
# best_individ_array_y.append(best_y)
#
# best_individ_z.append(population[index_y][:len_individ // 2])
# count_str_z.append(temp_count_fit_z / count_individ)
# best_individ_array_z.append(best_z)
#
#
# best_z = -math.inf
# best_y = -math.inf
#
# # >--------------------------------------------------------------------------------------------------------
# for i in range((count_generations - 1) * count_individ):  # Основной цикл создания популяций
#     #  while countc < len_individ:
# # >--------------------------------------------------------------------------------------------------------
#     fp = randint(0, len(population) - 1)  # Турнирный метод отбора родителей
#     sp = randint(0, len(population) - 1)
#
#     if population_fit_y[fp] >= population_fit_y[sp]:
#         parent_one = population[fp]
#     else:
#         parent_one = population[sp]
#
#     fp = randint(0, len(population) - 1)  # Турнирный метод отбора родителей
#     sp = randint(0, len(population) - 1)
#
#     if population_fit_y[fp] >= population_fit_y[sp]:
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
#         if rand <= mutation_probability:
#             child[i] = 1 if child[i] == 0 else 0
#     lst_fit_temp_y.append(fitness_one(child))
#     lst_fit_temp_z.append(fitness_two(child))
#     child_population.append(child)  # Добавление ребенка в список
#
# # >--------------------------------------------------------------------------------------------------------
#     best_y = -math.inf
#     best_z = -math.inf
#     if len(population) == len(child_population):
#         for i in range(len(population_fit_y)):
#             if best_y <= lst_fit_temp_y[i]:
#                 best_y = lst_fit_temp_y[i]
#                 index_y = i
#             temp_count_fit_y += lst_fit_temp_y[i]
#
#         for i in range(len(population_fit_z)):
#             if best_z <= population_fit_z[i]:
#                 best_z = population_fit_z[i]
#                 index_z = i
#             temp_count_fit_z += population_fit_z[i]
#
#         best_individ_array_y.append(best_y)
#         count_str_y.append(temp_count_fit_y / count_individ)
#         best_individ_y.append(child_population[index_y])
#
#         best_individ_z.append(population[index_y][:len_individ // 2])
#         count_str_z.append(temp_count_fit_z / count_individ)
#         best_individ_array_z.append(best_z)
#
#         population_fit_y = lst_fit_temp_y.copy()
#         population_fit_z = lst_fit_temp_z.copy()
#
#         population = child_population.copy()
#         child_population = []
#
#         lst_fit_temp_y = []
#         lst_fit_temp_z = []
#         best_y = -math.inf
#         best_z = -math.inf
#     temp_count_fit_y = 0
#     temp_count_fit_z = 0
#
# # >--------------------------------------------------------------------------------------------------------
#
# for ex in range(len(count_str_y) + 1):
#     count_str_x = list(range(1, ex + 1))
#
#
# for i in best_individ_y:
#     best_individ_x_one.append(float_number(i))
#
#
# # >--------------------------------------------------------------------------------------------------------
# # print(count_str_y, 'count str ')
# # print(best_individ_y, 'best_y count_individ')
# # print(child, 'child')
# # >--------------------------------------------------------------------------------------------------------
#
# ax = plt.axes(projection="3d")
# x = best_individ_x_one
# y = best_individ_array_y
# z = best_individ_array_z
# ax.scatter(x, y, z)
#
#
#
# plt.show()
#
#
# # figure, axis = plt.subplots()
# # x_one = np.linspace(limit_one, limit_two, 50)
# # y_one = [function(i) for i in x_one]
# # x = best_individ_x_one
# # y = best_individ_array_y
# #
# # plt.scatter(x, y, 20)
# # axis.plot(x_one, y_one)
# # plt.show()
# # print(x , 'x')
# # print(y, 'y')

#
# import math
# from random import randint, random
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d.art3d import Poly3DCollection
#
# temp_count_fit = 0
# child = []
# # count = 0
# # count2 = 0
# best = 0
# parent_one = []
# parent_two = []
# population = []
# countc = 0
# count_str = []
# individ = int(input("сколько хотите индивидов?  "))
# len_individ = int(input("длина индивидов  "))
# steps = int(input("кол-во поколений  "))
# mutation_veriety = float(input("вероятность мутации   "))
# sep_population = []
# count_str_x = []
# best_p = []
# best_count = 0
# population_fit = []
# lst_fit_x = []
# lst_fit_temp = []
# best_individ = []
# best_individ_x_one = []
# best_individ_x2 = []
#
# limit_one = int(input("ограничение 1 "))
# limit_two = int(input("ограничение 2 "))
# best = -math.inf
#
# # >--------------------------------------------------------------------------------------------------------
#
# def fi(x, x2):
#     return -((x**2) +
#
# def fitness(indiv):
#     s_individ = "".join(map(str, indiv))
#     int_individ = int(s_individ, 2)
#     float_individ = (int_individ / (2 ** len(indiv) - 1)) * (limit_two - limit_one) + limit_one
#     float_individ_y = fi(float_individ)
#     # print(float_individ, float_individ_y)
#     return float_individ_y
#
# def fitness_x(indiv):
#     s_indiv = "".join(map(str, indiv))
#     int_individ = int(s_indiv, 2)
#     float_individ = (int_individ / (2 ** len(indiv) - 1)) * (limit_two - limit_one) + limit_one
#     return float_individ
#
#
# def fitness_x2(indiv):
#     s_indiv = "".join(map(str, indiv))
#     int_individ = int(s_indiv, 2)
#     float_individ_2 = (int_individ / (2 ** len(indiv) - 1)) * (limit_two - limit_one) + limit_one
#     return float_individ_2
# # >--------------------------------------------------------------------------------------------------------
#
# for i in range(individ):
#     num_child = []
#     for i in range(len_individ):
#         a = randint(0, 1)
#         num_child.append(a)
#     population.append(num_child)
#
#
#
# for i in population:
#     population_fit.append(fitness(i))
#
#
# for i in range(len(population_fit)):
#     if best <= population_fit[i]:
#         best = population_fit[i]
#         index_ = i
#     temp_count_fit += population_fit[i]
#
# best_individ.append(population[index_])
# count_str.append(temp_count_fit / individ)
# best_p.append(best)
# best = -math.inf
#
# # >--------------------------------------------------------------------------------------------------------
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
#         if rand <= mutation_veriety:
#             child[i] = 1 if child[i] == 0 else 0
#     lst_fit_temp.append(fitness(child))
#     sep_population.append(child)  # Добавление ребенка в список
#
# # >--------------------------------------------------------------------------------------------------------
#     best = -math.inf
#     if len(population) == len(sep_population):
#         for i in range(len(population_fit)):
#             if best <= lst_fit_temp[i]:
#                 best = lst_fit_temp[i]
#                 index_ = i
#             temp_count_fit += lst_fit_temp[i]
#
#         best_p.append(best)
#         count_str.append(temp_count_fit / individ)
#         best_individ.append(sep_population[index_])
#
#         population_fit = lst_fit_temp.copy()
#         population = sep_population.copy()
#         sep_population = []
#         lst_fit_temp = []
#         best = -math.inf
#     temp_count_fit = 0
#     #  print(population, "популяция")
#
#     print(population)
#
# # >--------------------------------------------------------------------------------------------------------
#
# for ex in range(len(count_str) + 1):
#     count_str_x = list(range(1, ex + 1))
#
#
# for i in best_individ:
#     best_individ_x_one.append(fitness_x(i))
#
# for i in best_individ:
#     best_individ_x2.append(fitness_x2(i))
#
#
# # >--------------------------------------------------------------------------------------------------------
# print(count_str, 'count str ')
# print(best_individ, 'best individ')
# print(child, 'child')
# # >--------------------------------------------------------------------------------------------------------
#
#
# ax = plt.axes(projection="3d")
# x = best_individ_x_one
# y = best_individ_x2
# z = best_p
# ax.scatter(x, y, z)
#
#
#
# plt.show()
#
# # figure, axis = plt.subplots()
# # x_one = np.linspace(limit_one, limit_two, 50)
# # y_one = [fi(i) for i in x_one]
# # x = best_individ_x_one
# # y = best_p
# #
# # plt.scatter(x, y, 20)
# # axis.plot(x_one, y_one)
# # plt.show()
# # print(x , 'x')
# # print(y, 'y')

# from calendar import c
# from os import sep


import math
from random import randint, random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



temp_count_fit = 0                    # Среднее значение float в итерации
child = []                            # Ребёнок
# count = 0
# count2 = 0
best = 0                              # Сравнительная переменная (min\max)
parent_one = []                       # 1 Участник в генерации потомка
parent_two = []                       # 2 Участник в генерации потомка
population = []                       # Оснвной массив популяции
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
best_individ_x_one = []
best_individ_x_two = []
limit_one = int(input("ограничение 1 "))
limit_two = int(input("ограничение 2 "))
best = -math.inf

# >--------------------------------------------------------------------------------------------------------
def function(x1, x2):
    return -(x1 ** 2 + x2 ** 2)                                 # Задание фунции

# def function(x):
#     return -(x-2)**2

def fitness_one(indiv):                                         # Значение Y (Z)
    s_indiv = "".join(map(str, indiv))
    int_individ_one = int(s_indiv[:len(s_indiv) // 2 + 1], 2)
    int_individ_two = int(s_indiv[len(s_indiv) // 2:], 2)

    float_individ_one = (int_individ_one / (2 ** (len(indiv) / 2) - 1)) * (limit_two - limit_one) + limit_one
    float_individ_two = (int_individ_two / (2 ** (len(indiv) / 2) - 1)) * (limit_two - limit_one) + limit_one  # Значение

    # print(float_individ_one, float_individ_two)

    float_individ_y = function(float_individ_one, float_individ_two)
    return float_individ_y

def float_number(indiv):                                        # Tuple X1, X2 (X, Y)
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
for i in best_individ:
    best_individ_x_two.append(float_number(i)[1])




# >--------------------------------------------------------------------------------------------------------
# print(count_str, 'count str ')
# print(best_individ, 'best_y count_individ')
# print(child, 'child')
# >--------------------------------------------------------------------------------------------------------
# figure, axis = plt.subplots()

#
# axis = figure.add_subplot(111, projection='3d')
# x = best_individ_x_one
# y = best_individ_array
# z = best_individ_x_two
#
# x1 = np.linspace(limit_one, limit_two, 50)
# y1 = np.linspace(limit_one, limit_two, 50)
# z1 = [function(i, k) for i, k in zip(x1, y1)]
# x1, y1 = np.meshgrid(x1, y1)
# axis.plot_surface(x1, y1, z1, color="red")
#
# axis.scatter(x, y, z)
# plt.show()

# x_one = np.linspace(limit_one, limit_two, 50)
# y_one = [function(i) for i in x_one]
# x = best_individ_x_one
# y = best_individ_array
#
# plt.scatter(x, y, 20)
# axis.plot(x_one, y_one)
# plt.show()
# print(x , 'x')
# print(y, 'y')

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

fig, ax = plt.subplots(subplot_kw={'projection':'3d'})

x1 = best_individ_x_one
y1 = best_individ_x_two
z1 = best_individ_array
plt.scatter(x1, z1, y1, c='b')

print(population)

plt.show()