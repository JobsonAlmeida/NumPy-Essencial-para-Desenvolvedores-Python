import numpy as np

array_3d = np.arange(1,25).reshape(2,4,3)

print(array_3d)
print(type(array_3d[0,0,0]))

print(array_3d.tolist())

print(array_3d.item(14))
print(type(array_3d.item(14)))

array_3d.itemset(14, 50)
print(array_3d)
print(array_3d.item(14))
print(type(array_3d.item(14)))

array_3d.itemset((1,0,2), 100)
print(array_3d)

print("----")

array_3d = np.arange(1,25).reshape(2,4,3)
print(array_3d)
array_view = array_3d.view()
print(array_view)

array_view[0,0,0] = 0


print("---")
array_1 = np.array([1,2,3,4,5])
array_2 = array_1.view()
print(id(array_1))
print(id(array_2))
print(np.shares_memory(array_1, array_2))
print(id(array_1[0]))
print(id(array_2[0]))

# array_3 = array_1
# print(array_3 is array_1)
# print(id(array_3[0]))
# print(id(array_1[0]))
# print(np.shares_memory(array_1, array_2))

print("---")
array_3d = np.arange(1,25).reshape(2,4,3)
array_copy = array_3d.copy()
print(array_copy)
array_copy[0,0,0] = 99
print(array_copy)
print("array_3d: \n")
print(array_3d)

array_3d.fill(55)
print(array_3d)



