import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab


# line 

x = np.linspace(0, 10, 500)
dashes = [10, 5, 100, 5]  # 10 points on, 5 off, 100 on, 5 off

fig, ax = plt.subplots()
line1, = ax.plot(x, np.sin(x), '--', linewidth=2,
                 label='funcion seno')
line1.set_dashes(dashes)
line2, = ax.plot(x, -1 * np.sin(x), dashes=[30, 5, 10, 5],
                 label='funcion coseno')
ax.legend(loc='lower right')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('LINE')
fig.savefig('line.png')
plt.close()
fig.clear()




fig, ax = plt.subplots()
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('SCATTER')
fig.savefig('scatter.png')
plt.close()



# HIST

from numpy.random import beta

plt.style.use('bmh')
def plot_beta_hist(ax, a, b):
    ax.hist(beta(a, b, size=10000), histtype="stepfilled",
            bins=25, alpha=0.8, density=True)


fig, ax = plt.subplots()
plot_beta_hist(ax, 10, 10)
plot_beta_hist(ax, 4, 12)
plot_beta_hist(ax, 50, 12)
plot_beta_hist(ax, 6, 55)
ax.set_xlabel('x')
ax.set_ylabel('PDF')
ax.set_title("HISTOGRAMA")

fig.savefig('hist.png')
plt.close()






plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = ('Mucho', 'suficiente', 'regular', 'poco', 'nada')
y_pos = np.arange(len(people))
performance = [12, 5, 3, 2, 1] #3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center',
        color='green', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Cantidad')
ax.set_title('Grado de satisfacción con la materia de computación')

fig.savefig('bars.png')
plt.close()







from __future__ import division

import matplotlib.pyplot as plt
from matplotlib import colors as mcolors


colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)

# Sort colors by hue, saturation, value and name.
by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
                for name, color in colors.items())
sorted_names = [name for hsv, name in by_hsv]

n = len(sorted_names)
ncols = 5
nrows = n // ncols + 1




fig, ax = plt.subplots(figsize=(9, 7))

# Get height and width
X, Y = fig.get_dpi() * fig.get_size_inches()
h = Y / (nrows + 1)
w = X / ncols

for i, name in enumerate(sorted_names):
    col = i % ncols
    row = i // ncols
    y = Y - (row * h) - h

    xi_line = w * (col + 0.15)
    xf_line = w * (col + 0.4)
    xi_text = w * (col + 0.4)

    ax.text(xi_text, y, name, fontsize=(h * 0.6),
            horizontalalignment='left',
            verticalalignment='center')

    ax.hlines(y + h * 0.1, xi_line, xf_line,
              color=colors[name], linewidth=(h * 0.8))

ax.set_xlim(0, X)
ax.set_ylim(0, Y)
ax.set_axis_off()

fig.subplots_adjust(left=0, right=1,
                    top=1, bottom=0,
                    hspace=0, wspace=0)
plt.show()
