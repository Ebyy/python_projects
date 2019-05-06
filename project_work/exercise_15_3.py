import  matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()

    # Set the size of the plotting window(dpi or specified figsize can be used).
    plt.figure(figsize=(13,8))


    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1,zorder=1)

    # Emphasize start and stop points
    # ((add to both) zorder is used to order the plotting so the one with
    # the higher order is on top not covered by the other plot).
    plt.scatter(0,0,c='green',edgecolors='none',s=80,zorder=2)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',
    edgecolors='none',s=80,zorder=2)

    #Remove axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another plot? (y/n): ")
    if keep_running == 'n':
        break