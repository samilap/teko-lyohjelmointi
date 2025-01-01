import numpy as np

x=np.array([1,2])
y=np.array([-1,2])

print('x shape =', np.shape(x))
print('y shape =', np.shape(y))

#ei toimi ku pitäs olla 2x2 matriisi lopuksi
print('x^T y =', x.transpose()@y)
