import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Generate color coded plot
while True:
    # Additional points can also be added by specifying
    rw = RandomWalk(50000)
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
    cmap=plt.cm.Blues, edgecolors='none', s=1)

    # The first and last points can also be empasized.
    plt.scatter(0,0,c='green',edgecolors='none',s=50)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',
    edgecolors='none',s=50)


    # Both AXES at x and y can also be REMOVED.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    # To alter the size of the screen
    plt.figure(dpi=128, figsize=(16,9))

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
