import matplotlib.pyplot as plt


x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Oranges,s=20)
plt.title("Cubed Numbers", fontsize=12)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Cubed Value", fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.axis([0,5500,0,150000000000])

# bbox cmd removes the excess white space around the plot
plt.savefig('exercise_15_1ii.png', bbox='thick')