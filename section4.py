import numpy as np


print( np.zeros(shape=3) )
print( np.zeros(shape=(1,3)).dtype )

print(np.ones(shape=(2,3)))

print(np.full(shape=(2,3), fill_value=4))

array = np.array([[1,2,3],
                  [4,5,6]])

print(array.shape)

print(np.zeros_like(a=array))
print(np.ones_like(a=array))
print(np.full_like(a=array, fill_value=4))

print(np.empty(shape=(2,3)))

print(np.eye(N=5))

print(np.eye(N=5, M=3))

print(np.identity(n = 5))


print(np.arange(stop=10))
print(np.arange(start=3, stop=10))
print(np.arange(start=3, stop=10, step=2))
print(np.arange(start=3, stop=10, step=3))
print(np.arange(start=10, stop=3, step=-2))
print(np.arange(start=3, stop=5, step=0.25))

print(np.linspace(start=1, stop=10, num=4))
print(np.linspace(start=1, stop=10, num=10))
print(np.linspace(start=1, stop=10, num=7))


print(np.logspace(start=1, stop=4, num=4))

print(np.geomspace(start=3, stop=48, num=5))