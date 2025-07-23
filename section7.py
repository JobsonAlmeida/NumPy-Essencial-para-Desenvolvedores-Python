import numpy as np

array_3d = np.arange(1,25).reshape(2, 4, 3)

array_take = array_3d.take(indices= [1,5,10,12])
print(array_take)
print(np.shares_memory(array_3d, array_take))

array_take_2d = array_3d.take(indices= [[1,5], [10, 12]])
print(array_take_2d)

print("----")
print(array_3d)
print("----")
array_3d.put(indices=[1,5,10,12], values=[52, 56, 61,63])
print(array_3d)


print("----")
array_3d = np.arange(1,25).reshape(2, 4, 3)

print(array_3d.repeat(repeats=3))

array_3d_rp_2_ax_0 = array_3d.repeat(repeats=2, axis=2)
print(array_3d_rp_2_ax_0)

print("----")

array_2d = np.array([[10, 3, 7],
                     [ 8, 2, 9]])
array_2d.sort(axis=0)
print(array_2d)

array_2d.sort(axis=1)
print(array_2d)
array_tranposed = array_2d.transpose()
print(array_tranposed)

print('---')
array_2d = np.array([[10, 3, 7],
                     [ 8, 2, 9]])

indices = array_2d.argsort(axis=1)
print(indices)


array_1d = np.array([4,1,2,3,5,0])
indices = array_1d.argsort()
print(indices)
print(array_1d[indices])

sorted_array = array_1d[indices]
print(sorted_array)

indices = sorted_array.searchsorted([1,4,11])
print(indices)
# sorted_array[indices] = [1,4,11]
print(sorted_array)

array_2d = np.array([[10,3,7],
                     [8,2,9],
                     [11,4,1]])

print(array_2d.diagonal())

