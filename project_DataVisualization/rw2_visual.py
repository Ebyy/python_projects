import  matplotlib.pyplot as plt

from random_walk2 import RandomWalk


while True:
    rw = RandomWalk()
    rw.fill_walk()

    # Increase screen display size.
    plt.figure(figsize=(13,7))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Oranges,s=5)

    # Emphasize start and stop points
    plt.scatter(0,0,c='green',edgecolors='none',s=70)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=70)

    #Remove axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Do you want to make another plot? (y/n): ")
    if keep_running == 'n':
        break