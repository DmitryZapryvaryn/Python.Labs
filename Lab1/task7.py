import numpy as np

a = np.arange(12)
b = a
print('b is a: ', b is a)  # проверяем, что b - это a
b.shape = 3, 4
print('b.shape: ', b.shape)
print('a.shape: ', a.shape)


def f(x):
    print('id f(x): ', id(x))
print('id a: ', id(a))
f(a)

c = a.view()
print('c is a: ', c is a)
print('c.base is a', c.base is a)
print('c.flags.owndata : ', c.flags.owndata)
c.shape = 2, 6
print('a.shape: ', a.shape)
c[0, 4] = 1234
print('a after c[0, 4] = 1234:\n', a)
d = a.copy()
print('d is a: ', d is a)
print('d.base is a: ', d.base is a)
d[0, 0] = 9999
print('a after d[0, 0] = 9999: ', a)
