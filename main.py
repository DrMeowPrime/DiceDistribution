from helper import *

dice_sides = int(input("Number of sides on each die: ")) # 20
rolls = int(input("Number of dice to roll per trial: ")) # 100
iterations = int(input("Number of trials to perform: ")) # 10000

init_sample = run_simulation(dice_sides, rolls, iterations)
mean, standard_dev, variance, test_sum = calculate(init_sample)

# print(init_sample)
print("\nDice Sides:", dice_sides, "  Rolls per trial:", rolls, "  Total trials:", iterations)
print("Mean: ", mean)
print("Standard Deviation: ", standard_dev)
print("Variance: ", variance)

plt.rcParams.update({'figure.figsize': (7, 5), 'figure.dpi': 100})
plt.hist(test_sum, bins=30)
plt.gca().set(title='Dice Frequency Histogram', ylabel='Frequency', xlabel='Sum of Dice Rolls')
plt.show()
