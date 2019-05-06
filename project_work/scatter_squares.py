import matplotlib.pyplot as plt


# Plot a point on the graph
plt.scatter(2,4,s=200)

plt.title("Square Numbers", fontsize=18)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()