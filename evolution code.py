import numpy as np
import random
import math
import plotly.express as px
import plotly.graph_objects as go


child_popultaion = []
population = []
len_indiv = int(input('Длина индивидов: '))
len_population = int(input('Длина популяции: '))
iterations = int(input('Количество итераций: '))
mutation_probability = float(input('Вероятность мутации: '))
limit_one = int(input('lim1: '))
limit_two = int(input('lim2: '))
search_input = input('max \ min: ')
if search_input == 'max':
    best = -math.inf
elif search_input == 'min':
    best = math.inf

best_individs = []

def function(x, y):
    return np.cos(x + y)


def fitness(indiv):
    s_indiv = "".join(map(str, indiv))
    i1 = int(s_indiv[:len(s_indiv) // 2], 2)
    i2 = int(s_indiv[len(s_indiv) // 2:], 2)
    x = (i1 / (2 ** (len(indiv) / 2) - 1)) * (limit_two - limit_one) + limit_one
    y = (i2 / (2 ** (len(indiv) / 2) - 1)) * (limit_two - limit_one) + limit_one

    z = function(x, y)
    return x, y, z


def population_fitness(pop):
    if search_input == 'max':
        best = -math.inf
        for indiv in pop:
            if fitness(indiv)[2] >= best:
                best = fitness(indiv)[2]
                best_indivd = indiv
        return best_indivd, best

    elif search_input == 'min':
        best = math.inf
        for indiv in pop:
            if fitness(indiv)[2] <= best:
                best = fitness(indiv)[2]
                best_indivd = indiv
        return best_indivd, best


def create_individ(x):
    individ = []
    for _ in range(x):
        individ.append(random.randint(0, 1))
    return individ


def selection(a, b):
    if fitness(a)[2] >= fitness(b)[2]:
        return a
    else:
        return b


def child_creation(p1, p2):
    rand = random.randint(0, len_indiv - 1)
    fh = p1[:rand]
    sh = p2[rand::]
    child = fh + sh
    for l in range(len(child)):  # Метод мутации
        rand = random.random()
        if rand <= mutation_probability:
            child[l] = 1 if child[l] == 0 else 0
    return child


for i in range(len_population):
    population.append(create_individ(len_indiv))

best_individs.append(population_fitness(population)[0])

for i in range(iterations):
    if len(child_popultaion) == len(population):
        population = []
        population.extend(child_popultaion)
        child_popultaion = []
        best_individs.append(population_fitness(population)[0])

    for i in range(len_population):
        first_parent = selection(population[random.randint(0, len_population - 1)], population[random.randint(0, len_population - 1)])
        second_parent = selection(population[random.randint(0, len_population - 1)], population[random.randint(0, len_population - 1)])
        # print(fitness(first_parent)[2], fitness(second_parent)[2])
        child_popultaion.append(child_creation(first_parent, second_parent))

x = []
y = []
z = []

for i in best_individs:
    x.append(fitness(i)[0])
    y.append(fitness(i)[1])
    z.append(fitness(i)[2])


best_indiv = population_fitness(best_individs)[0]

print([(fitness(best_indiv)[0])], [(fitness(best_indiv)[1])], [(fitness(best_indiv)[2])])

fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers')])
fig.add_scatter3d(x=[(fitness(best_indiv)[0])],
                  y=[(fitness(best_indiv)[1])],
                  z=[(fitness(best_indiv)[2])])

x1 = np.outer(np.linspace(limit_one, limit_two, 100), np.ones(100))
y1 = x1.copy().T
z1 = function(x1, y1)
fig.add_trace(go.Surface(x=x1, y=y1, z=z1, colorscale='Blues'))


fig.show()

