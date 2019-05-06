import pygal

from die_class import Die


# Create three D6 dice
die_1 = Die()
die_2 = Die()
die_3 = Die()

#Make some rolls of the dice, 2000 times
results = []
for roll_num in range(2000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_results = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3,max_results+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling 3 D6 dice 2000 times"
hist.x_labels = [str(x) for x in range(3,max_results+1)]
hist.x_title = "Reaults"
hist.y_title = "Frequency of Result"

hist.add('D6+D6+D6', frequencies)
hist.render_to_file('exercise_15_8_visual.svg')