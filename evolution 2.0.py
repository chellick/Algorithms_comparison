from random import randint
from random import randint
import numpy as np
import matplotlib.pyplot as plt
population = []
sep_population = []

kol = int(input("введите коливество индивидов: "))
dlin = int(input("введите длину индивидов: "))
times = int(input("введите желаемое количество популяцй: "))
count = 0
count2 = 0
parent1 = 0
parent2 = 0
child = []
fp = []
sp = []
for i in range(kol):
     first_people = []
     for i in range(dlin):
          a = randint(0, 1)
          first_people.append(a)
     population.append(first_people)
print(*population, sep="\n")
#  for i in range(times):

first_player = population[randint(0, len(population)) - 1]
second_player = population[randint(0, len(population)) - 1]

for i in first_player:
     if i == 1:
          count += 1
for i in second_player:
     if i == 1:
          count2 += 1
if count > count2:
     parent1 = first_player
elif count > count2:
     parent1 = second_player
elif count == count2:
     parent1 = first_player

count, count2 = 0, 0
first_player = population[randint(0, len(population)) - 1]
second_player = population[randint(0, len(population)) - 1] #  print(first_player, second_player)


for i in first_player:
     if i == 1:
          count += 1
for i in second_player:
     if i == 1:
          count2 += 1
if count > count2:
     parent2 = first_player
elif count > count2:
     parent2 = second_player
elif count == count2:
     parent2 = first_player

print(parent1, "par1", parent2, "par2")
part = randint(0, len(parent1) - 1)
fp = parent1[:part]
sp = parent2[part:]


child = str(fp) + str(sp)
sep_population.append(child)
print(sep_population)

#  print(child, "ребёнок") 


     
     



