import matplotlib.pyplot as plt


# To plot a series of points,
# a series of x and y-values are passed to python

x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]

plt.scatter(x_values,y_values,s=100)

plt.title("Square Numbers", fontsize=20)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square Value", fontsize=14)

plt.tick_params(axis='both',which='major', labelsize=14)


plt.show()