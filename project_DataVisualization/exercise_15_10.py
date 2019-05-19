import matplotlib.pyplot as plt

from die_class_pyplot import Die


# Create die
die_1 = Die()

# Make some rolls, 100 times.
results = []
for roll_num in range(100):
    result = die_1.roll()
    results.append(result)

# Analyze frequency of outcome

for value in range(1, die_1.num_sides+1):
    frequency = results.count(value)
    die_1.y_values.append(frequency)

die_1.x_values = [str(x) for x in range(1, die_1.num_sides+1)]

plt.plot(die_1.x_values, die_1.y_values, c='blue')
# Or plt.scatter(die_1.x_values, die_1.y_values, s=20)

plt.title("Results of a D6 die rolled 100 times", fontsize=20)
plt.xlabel("Result", fontsize=14)
plt.ylabel("Frequency of Result", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)


plt.show()
