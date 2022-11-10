import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make the data
np.random.seed(3)
x = 4 + np.random.normal(0, 2, 240)
y = 4 + np.random.normal(0, 2, len(x))
# size and color:
sizes = np.random.uniform(15, 80, len(x))
colors = np.random.uniform(15, 80, len(x))

# plot
fig, ax = plt.subplots(figsize=(5, 3), layout='constrained') #Change to Size of the figure

ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100, facecolor='C0', edgecolor='k', marker='p') #Change to Color and border of "Markers" on figure
ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))
ax.set_xlabel('Windage')
ax.set_ylabel('Altitude');
ax.set_title('Arrows shot down range')
plt.show()