import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)
y = x
yy = x ** 2

fig = plt.figure()
ax = fig.gca()
ax.plot(x, y, 'r-')
ax.plot(x, yy, 'g-')
ax.set_title('Title')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(['y = x', 'y = x^2'])
ax.grid()
fig.show()