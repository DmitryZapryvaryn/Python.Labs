import numpy as np
import matplotlib.pyplot as plt

# создание окна для отрисовки
plt.figure(figsize=(8, 5), dpi=80)
# указание области отрисовки графика
plt.subplot(111)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C, color='blue', linewidth=2.5, linestyle='-', label='cosine')
plt.plot(X, S, color='red', linewidth=2.5, linestyle='-', label='sine')

# spines - линии границ графика
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# xaxis.set_ticks_position - установка положения деления для оси Ох
ax.xaxis.set_ticks_position('bottom')
# position[0] should be one of 'outward', 'axes', or 'data'
ax.spines['bottom'].set_position(('data', 0))
# yaxis.set_ticks_position - установка положения деления для оси Оy
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

# установка пределов отображения оси Ох
plt.xlim(X.min() * 1.1, X.max() * 1.1)
# подпись значений Ох: ([знаения], [подписи])
plt.xticks(
    [-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi], [
        r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

# установка пределов отображения оси Оy
plt.ylim(C.min() * 1.1, C.max() * 1.1)
# подпись значений Оy: ([знаения], [подписи])
plt.yticks([-1, 1], [r'$-1$', r'$+1$'])

# установка местоположения легенды
plt.legend(loc='upper left')

t = 2 * np.pi / 3
# пунтирная линия от (t, 0) до (t, cos(t))
plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=1.5, linestyle='--')
# точка (t, cos(t)) радиусом 50
plt.scatter([t, ], [np.cos(t), ], 50, color='blue')
# подпись точки
plt.annotate(
    # текст подписи; $$ - для вставки мат формул
    r'$sin(\frac{2\pi}{3})=-\frac{\sqrt{3}}{2}$',
    # место куда указывает стрелка
    xy=(t, np.sin(t)), xycoords='data',
    # координаты подписи относительно точки xy
    xytext=(10, 30), textcoords='offset points', fontsize=16,
    # задание стиля стрелки
    arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))

# пунтирная линия от (t, 0) до (t, sin(t))
plt.plot([t, t], [0, np.sin(t)], color='red', linewidth=1.5, linestyle='--')
# точка (t, sin(t))
plt.scatter([t, ], [np.sin(t), ], 50, color='red')
# подпись точки
plt.annotate(
    # текст подписи; $$ - для вставки мат формул
    r'$cos(\frac{2\pi}{3})=-\frac{1}{2}$',
    # место куда указывает стрелка
    xy=(t, np.cos(t)), xycoords='data',
    # координаты подписи относительно точки xy
    xytext=(-90, -50), textcoords='offset points', fontsize=16,
    # задание стиля стрелки
    arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))

plt.show()
