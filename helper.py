# Jay Is Coding :sunglasses:

import random
import string
import matplotlib.pyplot as plt
import pandas
import numpy as np


# Creates a standardized array of arrays according to the input with an inputted dice_size and inputted iteration of
# rolls per iteration.
# Sides, roll, and iterate should all be integers
# sides determines the amount of sides the simulated dice has
# roll determines the amount of rolls is done in one iteration
# iterate determines the amount of times the whole trial is repeated
# Exports a list of lists with all the data
def run_simulation(sides, roll, iterate):
    result = []
    temp = []
    for i in range(iterate):
        temp = []
        for j in range(roll):
            temp.append(random.randrange(1, sides + 1))
        result.insert(i, temp)
    return result


# Calculates the mean, standard deviation, and the variance of the inputted data
# sample_data should be a list of lists, exports 3 floating point values
# Kinda super inefficient, runs at O(n^2), very poor for large sample sizes, but hey, it's not like I have a time
# constraint on creating these, I'm writing this as a wait for one with 10,000,000 trials generate, my computer
# is seriously chugging, the fans are going wild
# Would recommend keeping the trials limited to around 100,000 unless you have several minutes to spare
def calculate(sample_data):
    use_data = sum_arrays(sample_data)
    average_mean = 0
    for i in range(len(use_data)):
        average_mean += use_data[i]
    average_mean = average_mean / len(sample_data)
    average_standard_dev = np.std(use_data)
    variance = np.square(average_standard_dev)
    return average_mean, average_standard_dev, variance, use_data


# Sums the arrays inside the arrays to get their total "score" this score is then used later in the graphing process
# to show the distribution of rolls
def sum_arrays(array):
    sum = []
    count = len(array[0])
    for i in range(len(array)):
        temp_sum = 0
        for j in array[i]:
            temp_sum += j
        sum.insert(i, temp_sum)
    return sum
