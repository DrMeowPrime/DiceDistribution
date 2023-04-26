from helper import *

dice_sides = 20
rolls = 100
iterations = 100000

init_sample = run_simulation(dice_sides, rolls, iterations)
mean, standard_dev, variance = calculate(init_sample)

# print(init_sample)
print("Dice Sides:", dice_sides, "  Rolls per trial:", rolls, "  Total trials:", iterations)
print("Mean: ", mean)
print("Standard Deviation: ", standard_dev)
print("Variance: ", variance)
test_sum = sum_arrays(init_sample)

plt.rcParams.update({'figure.figsize': (7, 5), 'figure.dpi': 100})
plt.hist(test_sum, bins=30)
plt.gca().set(title='Dice Frequency Histogram', ylabel='Frequency', xlabel='Sum of Dice Rolls')
plt.show()
