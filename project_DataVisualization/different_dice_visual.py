import pygal

from die_class import Die


# Create D6 and D10 dice
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store the results.
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()
hist.title = "Results of rolling a D6 and D10 50000 times"
# Another way to assign the values in hist.x_labels using a loop.
# [str(x) for x in range(2,max_result+1)]
hist.x_labels = []
for x in range(2,max_result+1):
    hist.x_labels.append(str(x))
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add('D6 + D10',frequencies)
hist.render_to_file('different_dice_visual.svg')
