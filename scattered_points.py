import matplotlib.pyplot as plt

plt.scatter(2 , 4 , s=100)

plt.title("DOt", fontsize=13)
plt.xlabel("val", fontsize=13)
plt.ylabel("sqval", fontsize=13)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()