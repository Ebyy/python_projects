import pygal

from die_class import Die


# Create 2 dice
die_1 = Die()
die_2 = Die(8)

# Make some rolls but multiply outcomes
results = []
for roll_num in range(1000):
    result = die_2.roll() * die_1.roll()
    results.append(result)

# Analyze the results
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling two dice 1000 times"
hist.x_labels = [str(x) for x in range(1, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of the Result"

hist.add('D6 * D8', frequencies)
hist.render_to_file('exercise_15_9_visual.svg')
