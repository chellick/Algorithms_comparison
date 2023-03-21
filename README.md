# Gen algorythm *VS* particle swarm optimisation

## Hypothesis

My hypothesis is this: a population adapts better over generations than under the influence of social factors.

## Purpose and tasks of the work

Analysis of the efficiency of global optimization algorithms on test functions and development of their modifications in order to increase efficiency.
During the development of the project roadmap, the following tasks were set:

1. Implementation of a standard genetic algorithm in Python.
2. Adapting the genetic algorithm to solve the problem of calculating the global extrema of a function.
3. Obtaining a solution and values.
4. Implementation of the swarm method in Python.
5. The study of various modifications of both algorithms in order to improve the efficiency of solving this problem.
6. Comparison of the operation of two global optimization algorithms.

## Genetic algorithm

Genetic Algorithm, known as GA or GA, is a search technique used to solve global optimization problems. It is based on mechanisms similar to natural selection in nature and is a kind of evolutionary computation. This method uses evolutionary selection methods such as inheritance, mutation, selection, and crossing over to achieve better optimization.
To solve the problem of finding local extrema of a function, an algorithm based on the classical genetic algorithm of John Holland is used. The work of the algorithm can be divided into several stages:

1. first generation generation
2. selection of parents
3. crossing
4. mutations
5. creating a new generation

Items 2-5 are performed until the specified number of generations has passed.
In the *FGEF* problem (finding the global extremum of a function), a binary string with a given length is taken as an individual. The characteristic of comparison, in turn, is the number of units in a given individual. The population is an array with N-specified number of elements.

