import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Generates multiple random walks but
# get prompted about continuing when you close the chart
while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.scatter(rw.x_values, rw.y_values, s=10)
    plt.show()

    # Inquire if user wants to quit or continue
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
