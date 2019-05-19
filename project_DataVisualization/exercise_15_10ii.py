import pygal

from random_walk import RandomWalk

rw = RandomWalk(100)
rw.fill_walk()

hist = pygal.Bar()

hist.title = "Results of a random walk"
hist.add('steps', rw.y_values)
hist.render_to_file('randomwalk_pygal_visual.svg')
