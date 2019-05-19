import matplotlib.pyplot as plt


x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values, edgecolor='none', c=(0,0.8,0.9), s=40)
# the tuple assign to c can always be adjusted with values from 0 to 1
#the closer a value is to 0 the darker the color of the plotted line and viz versa

plt.title("Square Numbers", fontsize=14)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis
plt.axis([0,1100,0,1100000])

# To remove outlines from data points with the edgecolor

plt.show()