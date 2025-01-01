import numpy as np

# Luodaan vektorit matriiseina (2d taulukosta)
#   (1) (-1 2).
#    2

x=np.array([1,2], ndmin = 2)
y=np.array([-1,2], ndmin = 2)

print('x shape =', np.shape(x))
print('y shape =', np.shape(y))

#ei toimi ku pitäs olla 2x2 matriisi lopuksi
print('x^T y =', x.transpose()@y)
