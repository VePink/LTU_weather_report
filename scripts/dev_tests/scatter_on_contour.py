import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
Z = 10.0 * (Z2 - Z1)

norm = cm.colors.Normalize(vmax=abs(Z).max(), vmin=-abs(Z).max())
cmap = cm.PRGn

levels = np.arange(-2.0, 1.601, 0.4)

fig, axes = plt.subplots(1,2, sharey=True)

for ax, zord in zip(axes, [1, -1]):
    ax.contourf(X, Y, Z, levels,
                cmap=cm.get_cmap(cmap, len(levels)-1),
                norm=norm)
    ax.autoscale(False) # To avoid that the scatter changes limits
    ax.scatter(np.random.uniform(-3,3,10),
               np.random.uniform(-2,2,10),
               zorder=zord)
    ax.set_title('Scatter with zorder={0}'.format(zord))