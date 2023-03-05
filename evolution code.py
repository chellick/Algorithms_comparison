import numpy as np
import random
import math
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px


child_popultaion = []
population = []
len_indiv = int(input('Длина индивидов: '))
len_population = int(input('Длина популяции: '))
iterations = int(input('Количество итераций: '))
mutation_probability = float(input('Вероятность мутации: '))
limit_one = float(input('lim1: '))
limit_two = float(input('lim2: '))
search_input = input('max \ min: ')
if search_input == 'max':
    best = -math.inf
elif search_input == 'min':
    best = math.inf

best_individs = []

mconst = mutation_probability

best_iteration = [best, 0]
SConst = 0.05


mutation_list = []


def function(x: float, y: float) -> float:
    # return -(x ** 2 + y ** 2)
    # return np.cos(x + y)
    # return 0.1 * x ** 2 + 0.1 * y ** 2 - 4 * np.cos(0.8 * x) - 4 * np.cos(0.8 * y) + 8
    # return x ** 2 + (y + 1) ** 2 - 5 * np.cos(1.5 * x + 1.5) - 3 * np.cos(2 * y - 1.5)
    # return -np.sin(10 * (x ** 2 + y ** 2))
    # return 10 * 2 + ((y ** 2 - 10 * np.cos(2 * np.pi)) + (y ** 2 - 10 * np.cos(2 * np.pi)))
    # return (x + y) ** 2 * (x + y) ** 2 
    return 10 * 2 + (x ** 2 - 10 * np.cos(2 * np.pi * x) + (y ** 2 - 10 * np.cos(2 * np.pi * y)))


def fitness(indiv: list) -> tuple:
    s_indiv = "".join(map(str, indiv))
    i1 = int(s_indiv[:len(s_indiv) // 2], 2)
    i2 = int(s_indiv[len(s_indiv) // 2:], 2)
    x = (i1 / (2 ** (len(indiv) / 2) - 1)) * (limit_two - limit_one) + limit_one
    y = (i2 / (2 ** (len(indiv) / 2) - 1)) * (limit_two - limit_one) + limit_one

    z = function(x, y)
    return x, y, z


def population_fitness(pop: list) -> tuple:
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


def create_individ(x: int) -> list:
    individ = []
    for _ in range(x):
        individ.append(random.randint(0, 1))
    return individ


def selection(a:list, b:list) -> list:
    if fitness(a)[2] >= fitness(b)[2]:
        return a
    else:
        return b

def get_av_fitness(population: list) -> int:
    res = 0
    for individ in population:
        res += fitness(individ)[2]
    return res / len(population)


def get_worst(population: list) -> list:
    if search_input == 'max':
        worst = (fitness(population[0])[2], 0)
        for ind in range(1, len(population)):
            if fitness(population[ind])[2] < worst[0]:
                worst = (fitness(population[ind])[2], ind)
        return worst


    if search_input == 'min':
        worst = (fitness(population[0])[2], 0)
        for ind in range(1, len(population)):
            if fitness(population[ind])[2] > worst[0]:
                worst = (fitness(population[ind])[2], ind)
        return worst



def child_creation(p1: list, p2: list) -> list:
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

        if search_input == 'max':
            if population_fitness(population)[1] > best_iteration[0]:
                best_iteration = [population_fitness(population)[1], i]

            # if get_av_fitness(population) > population_fitness(population)[1] - (population_fitness(population)[1] * SConst):
            #     mutation_probability += mconst * SConst
            # elif get_av_fitness(population) < population_fitness(population)[1] - (population_fitness(population)[1] * SConst):
            #     mutation_probability -= mconst * SConst 


        elif search_input == 'min':
            if population_fitness(population)[1] < best_iteration[0]:
                best_iteration = [population_fitness(population)[1], i]

            # if get_av_fitness(population) < population_fitness(population)[1] - (population_fitness(population)[1] * SConst):
            #     mutation_probability += mconst * SConst 
            # elif get_av_fitness(population) > population_fitness(population)[1] - (population_fitness(population)[1] * SConst):
            #     mutation_probability -= mconst * SConst 

        # print(best_iteration)
        mutation_list.append(mutation_probability)

#---------------------------------------------------------------------------------------------------

        # print(mutation_probability)
        # # print(get_av_fitness(population))
    
# ---------------------------------------------------------------------------------------------------
    for r in range(len_population):
        first_parent = selection(population[random.randint(0, len_population - 1)],
                                 population[random.randint(0, len_population - 1)])
        second_parent = selection(population[random.randint(0, len_population - 1)],
                                  population[random.randint(0, len_population - 1)])
        child_popultaion.append(child_creation(first_parent, second_parent))
    

x = []
y = []
z = []

for i in best_individs:
    x.append(fitness(i)[0])
    y.append(fitness(i)[1])
    z.append(fitness(i)[2])

best_indiv = population_fitness(best_individs)[0]

print(float(fitness(best_indiv)[2]))


# fig = px.line(y = mutation_list, x = range(0, len(mutation_list)))
# fig.show()


fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers')])
fig.add_scatter3d(x=[(fitness(best_indiv)[0])],
                  y=[(fitness(best_indiv)[1])],
                  z=[(fitness(best_indiv)[2])])

x1 = np.outer(np.linspace(limit_one, limit_two, 100), np.ones(100))
y1 = x1.copy().T
z1 = function(x1, y1)
fig.add_trace(go.Surface(x=x1, y=y1, z=z1, colorscale='Viridis'))


# pio.templates["custom_dark"] = pio.templates["plotly_dark"]
# pio.templates["custom_dark"]['layout']['paper_bgcolor'] = '#000000'
# pio.templates["custom_dark"]['layout']['plot_bgcolor'] = '#000000'
# pio.templates['custom_dark']['layout']['yaxis']['gridcolor'] = '#000000'
# pio.templates['custom_dark']['layout']['xaxis']['gridcolor'] = '#000000'
# pio.templates['custom_dark']['layout']['xaxis']['showgrid'] = False
# pio.templates['custom_dark']['layout']['yaxis']['showgrid'] = False
# # pio.templates['custom_dark']['layout']['colorway']['tickcolor'] = '#000000'
# fig.layout.template = 'custom_dark'

fig.show()


# 46.28978566816091
# 46.28978542327448
# 46.289786206352694
# 46.28978618209494
# 46.289786140944
# 46.28978618209494
# 46.289785377914534
# 46.28978598589301
# 46.289786206352694
# 46.28978571220181
# 46.2897859372568