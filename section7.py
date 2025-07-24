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


print("----")
array_2d = np.array([[4,2,12],
                     [10,5,6],
                     [1,11,9],
                     [7,8,3]])

print(array_2d)
print(array_2d.max(axis=0))
print(array_2d.max(axis=1))

array_2d_ax_1_kd = array_2d.max(axis=1, keepdims=True)
print(array_2d_ax_1_kd)

array_2d_ax_0_kd = array_2d.max(axis=0, keepdims=True)
print(array_2d_ax_0_kd)


print("---")
print(array_2d)
print(array_2d.max())
print(array_2d.argmax(axis=0))
print(array_2d.argmax())


print("---")
print(array_2d)
print(array_2d.min())
print(array_2d.argmin(axis=0))
print(array_2d.argmin())

print("---")
print(array_2d)
print(array_2d.ptp(axis=0))
print(array_2d.ptp(axis=1))
print(array_2d.ptp())

print('---')
array_2d = np.arange(1,13).reshape(4,3)
print(array_2d)
print(array_2d.clip(min=3.1, max=10))

array_2d = np.linspace(0,1,12).reshape(4,3)
print(array_2d)
array_round = array_2d.round(decimals=2)
print(array_round)

print("---")
array_2d = np.arange(1,13).reshape(4,3)
print(array_2d)
# # print(array_2d.sum(axis=0))
# # print(array_2d.sum(axis=1, keepdims = True))
# print(array_2d.cumsum(axis=0))
# print(array_2d.cumsum(axis=1))

print(array_2d.mean(axis=0))
print(array_2d.mean(axis=1))

print("---")
array_2d = np.arange(1,13).reshape(4,3)
print(array_2d)
print(array_2d.var(axis=0))
print(array_2d.var(axis=1))
print(array_2d.var())

print("---")
array_2d = np.arange(1,13).reshape(4,3)
print(array_2d.std(axis=0))
print(array_2d.std(axis=1))
print(array_2d.std())

print("---")
array_2d = np.arange(1,13).reshape(4,3)
print(array_2d)
print(array_2d.prod(axis=0))
print(array_2d.prod(axis=1))
print(array_2d.prod())

print(array_2d.cumprod(axis=0))
print(array_2d.cumprod(axis=1))
print(array_2d.cumprod())

print("---")
array_2d = np.arange(1,13).reshape(4,3)
print(array_2d)
array_2d_gt_0 = array_2d > 0
array_2d_gt_0.all(axis=0)

array_2d_gt_5 = array_2d > 5
print(array_2d_gt_0.all(axis=0))
print(array_2d_gt_5.all(axis=0))
print(array_2d_gt_0.any(axis=0))
print(array_2d_gt_5.any(axis=1))