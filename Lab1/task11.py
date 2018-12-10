import matplotlib.pyplot as plt
import numpy as np

# строит график (x, y); ro - задает цвет и тип линии (красные точки)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])  # задает границы осей [xmin, xmax, ymin, ymax]

plt.show()

t = np.arange(0., 5., 0.2)
# отрисовывает три (x, y) на одном графике;
# r-- - красные тире, bs - черные квадраты, g^ - зелёные треугольники
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
