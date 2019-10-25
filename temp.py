
from random import random
import matplotlib.pyplot as plt
import statistics
from numpy import std


# random.randrange() with two arguments to choose starting node
# print('Random number between 1 and 3 : ', random.randrange(1, 4))


class DrunkardWalk:

    def __init__(self, n, initial_state=0):
        self.n = n
        self.current_state = initial_state

    def is_absorbed(self):
        return self.current_state == 0 or self.current_state == self.n

    def move(self):
        if not self.is_absorbed():
            if random() > 0.5:
                self.current_state += 1
            else:
                self.current_state -= 1


# Parameters
MAX_STATE = 3
NUM_SIMULATIONS = 1000
BIN_PERCENTAGE = 0.1

# Simulation
time_to_absorb = []
for _ in range(NUM_SIMULATIONS):
    dw = DrunkardWalk(MAX_STATE, initial_state=MAX_STATE / 2)
    num_steps = 0
    num_visits = dict((i, 0) for i in range(MAX_STATE + 1))
    while not dw.is_absorbed():
        dw.move()
        num_visits[dw.current_state] += 1
        num_steps += 1
    time_to_absorb.append(num_steps)

# Basic statistics
print r"""
Statistics
----------
Max state  = %s
Mean       = %s
Median     = %s
Mode       = %s
Min        = %s
Max        = %s
Ã‰cart-type = %s
""" % (MAX_STATE, float(statistics.mean(time_to_absorb)), statistics.median(time_to_absorb),
       statistics.mode(time_to_absorb), min(time_to_absorb), max(time_to_absorb),
       float(std(time_to_absorb)))
