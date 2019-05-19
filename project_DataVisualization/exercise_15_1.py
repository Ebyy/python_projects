import matplotlib.pyplot as plt


x_values = [1,2,3,4,5]
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values,edgecolors='none', s=20)

plt.title("Cubed Numbers", fontsize=20)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Cubed Value", fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)

plt.show()