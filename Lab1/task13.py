import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0., 5., 0.2)
y = x**2
line, = plt.plot(x, y, '--', linewidth=2.0)
line.set_antialiased(False)
plt.show()

x1 = np.arange(0., 5., 0.2)
y1 = x1**(0.5)
x2 = np.arange(1., 5., 0.1)
y2 = x2**(2)

lines = plt.plot(x1, y1, x2, y2)
plt.setp(lines)
plt.setp(lines, color='r', linewidth=2.0)
# в стиле MATLAB
# plt.setp(lines, 'color', 'r', 'linewidth', 2.0)
plt.show()
