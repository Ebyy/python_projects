import matplotlib.pyplot as plt

from die_class import Die


# Create a die
die_1 = Die()

# Make some rolls with the die, 100 times
results = []
for roll_num in range(100):
    result = die_1.roll()
    results.append(result)

# Analyze the results
frequencies = []
for value in range(1, die_1.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
die_1.x_axis = [str(x) for x in range(1, die_1.num_sides+1)]

plt.plot(die_1.x_axis,frequencies,c='green')

plt.title('Results of rolling a D6 die 100 times')
plt.xlabel('Result', fontsize=14)
plt.ylabel('Frequency of Result', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
