import numpy as np

a = np.arange(10)**3
print(a)
print(a[2])
print(a[2:5])  # (2,5] - 3, 4, 5
a[:7:2] = -1000  # == (a[0:6:2] = -1000)

print(a)
print(a[::-1])
for i in a:
    print(np.sign(i) * (np.abs(i))**(1./3.))

print()
b = np.arange(20).reshape(5, 4)
print('b: ', b)
print('b[2, 3]: ', b[2, 3])
print('b[0:5, 1]:', b[0:5, 1])
print('b[:, 1]:', b[:, 1])
print('b[1:3,:]: ', b[1:3, :])
print('b[-1]', b[-1])

print()
c = np.array([[[0, 1, 2], [10, 12, 13]], [[100, 101, 102], [110, 112, 113]]])
print('c: ', c)
print('c[1, ...]: ', c[1, ...])
print('c[..., 2]: ', c[..., 2])

print()
print("each row from b: ")
for row in b:
    print(row)

print()
print("each element from b: ")
for element in b.flat:
    print(element)
