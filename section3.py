import numpy as np

# array_from_list = np.array([1,2,3])
# print(array_from_list)

list_a = [1,2,3]
# print(type(list_a))

array_from_list = np.array(list_a)
# print(array_from_list)
# print(type(array_from_list))

# tupla_a = (1,2,3)
# print(type(tupla_a))

# array_from_tuple = np.ndarray(tupla_a)
# print(type(array_from_tuple))

# set_a = {1,2,3,4}
# print(set_a)
# print(type(set_a))

# array_from_set = np.array(set_a)
# print(array_from_set)
# print(type(array_from_set))

# print(array_from_set.shape)


# array_from_set + 5


# dict_a = {1: 'a', 2: 'b'}
# print(dict_a)
# print(type(dict_a))

# array_from_dict = np.array(dict_a)
# print(array_from_dict)
# print(type(array_from_dict))
# print(array_from_dict.ndim)
# print(array_from_dict.shape)


# array_a = np.array(5)
# print(array_a)
# print(type(array_a))
# print(array_a.shape)
# print(array_a.ndim)

array_2d = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])

# print(array_2d)
# print(array_2d[0])

# print(array_2d[0][0])



array_3d = np.array([[ [ 1,  2,  3],
                       [ 4,  5,  6],
                       [ 7,  8,  9],
                       [10, 11, 12]],
                     
                     [ [13, 14, 15],
                       [16, 17, 18],
                       [19, 20, 21],
                       [22, 23, 24]]])

print(array_3d[0])


print(array_from_list.size)
print(array_2d.size)
print(array_3d.size)

print("---")
print(array_from_list.ndim)
print(array_2d.ndim)
print(array_3d.ndim)

print("---")
print(array_from_list.shape)
print(array_2d.shape)
print(array_3d.shape)

print( len(array_3d) )

print("---")
print(array_from_list.itemsize)
print(array_2d.itemsize)
print(array_3d.itemsize)

print("---")

print(array_from_list.size)
print(array_2d.size)
print(array_3d.size)

print(array_from_list.nbytes)
print(array_2d.nbytes)
print(array_3d.nbytes)

print("---")

print(array_from_list.dtype)
print(array_2d.dtype)
print(array_3d.dtype)

array_32bits = np.array([1,2,3], dtype=np.int32)
array_64bits = np.array([1,2,3], dtype=np.int64)

print("---")
print(array_32bits.dtype)


print("---")
print( np.array([1,2,3], dtype=np.float32).dtype )
print( np.array([1,2,3], dtype=np.str_).dtype )
print( np.array([1,2,3], dtype= float).dtype )