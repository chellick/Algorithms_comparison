from operator import attrgetter
import numpy as np
import random


def create_individ(x: int) -> list:
    individ = []
    for _ in range(x):
        individ.append(random.randint(0, 1))
    return individ

def function(x, y, *args):
    return 10 * 2 + (x ** 2 - 10 * np.cos(2 * np.pi * x) + (y ** 2 - 10 * np.cos(2 * np.pi * y)))




class Population():
    def __init__(self, length=10, bit_length=10, mutation=0.1, args=[], nargs=2, lim1=0, lim2=10):
        self.length = length
        self.blength = bit_length * nargs
        self.array = []
        self.mutation = mutation
        self.args = args
        self.nargs = nargs
        self.lim1 = lim1
        self.lim2 = lim2


    def get_attr(self):
        return self.length, self.blength, self.array, self.mutation

    def create_population(self):
        for _ in range(self.length):
            self.array.append(create_individ(self.blength))
        return 'Filled successfully'
    

    def fitness(self, indiv):
        s_indiv = "".join(map(str, indiv))
        for el in s_indiv:
            + = int(split_array(s_indiv)[i], 2)
            
 
    @staticmethod
    def split_array(arr, n):
        size = len(arr) // n
        result = []
        for i in range(n):
            result.append(arr[i*size:(i+1)*size])
        return result



    # def selection(self):
    #     for individ


    

    

popul = Population()

popul.create_population()

print(popul.get_attr())

