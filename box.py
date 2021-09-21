import matplotlib.pyplot as plt
slices = [32, 25, 6, 18, 12]
labels = 'C', 'Java', 'C++', 'Python', 'Dart'
plt.axes(aspect = 1)
explode = [0, 0, 0, 0.1, 0]
plt.pie(x = slices, labels = labels, autopct = '%1.1f %%', shadow = True, startangle = 120, explode = explode)
plt.show()