import numpy as np
import random


def function(args):
    # return 10 * 2 + (args[0] ** 2 - 10 * np.cos(2 * np.pi * args[1]) + (args[0] ** 2 - 10 * np.cos(2 * np.pi * args[1])))
    # return np.sin(args[1]) + np.sin(args[2]) + np.sin(args[3]) + np.sin(args[0])
    # return sum(np.sin(x) for x in args)
    return 10 * 2 + (args[0] ** 2 - 10 * np.cos(2 * np.pi * args[0]) + (args[1] ** 2 - 10 * np.cos(2 * np.pi * args[1])))
    # return (args[0] ** 2) + (2 * args[1] ** 2) + (3 * args[2] ** 2)
    # return sum([(i+1)*x**2 for i, x in enumerate(args)])