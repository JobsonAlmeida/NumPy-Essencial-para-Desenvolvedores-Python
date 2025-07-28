import numpy as np

array_1d = np.arange(0,10)
array_2d_0 = np.arange(0,18).reshape(3,6)
array_2d_1 = np.arange(18,36).reshape(3,6)

# print(array_2d_0)
# print("---")
# print(array_2d_1)

# print("---")
# array_concatenated = np.concatenate([array_2d_0, array_2d_1], axis=1)
# print(array_concatenated)
# print("---")
# array_stacked = np.stack(arrays=[array_2d_0, array_2d_1])
# print(array_stacked)
# print("---")
# array_stacked = np.stack(arrays=[array_2d_0, array_2d_1], axis=1)
# print(array_stacked)
# print("---")
# array_stacked = np.stack(arrays=[array_2d_0, array_2d_1], axis=-1)
# print(array_stacked)
# print(array_stacked.shape)

# print("---")
# array_vstack = np.vstack(tup= [array_2d_0, array_2d_1])
# print(array_vstack)

# print("---")
# array_vstack = np.hstack(tup= [array_2d_0, array_2d_1])
# print(array_vstack)

# print("---array 1d --- ")
# print(array_1d)
# array_split = np.split(ary=array_1d, indices_or_sections=2)
# print(array_split)
# print(len(array_split))
# print(array_split[0])

# print("--- array 2d ---")
# print(array_2d_0)
# array_split = np.split(ary=array_2d_0, indices_or_sections=3, axis=1)
# print(array_split)
# print(array_split[0])

# print("--- array 2d ---")
# print(array_2d_0)
# array_split = np.split(ary=array_2d_0, indices_or_sections=[2,3], axis=1)
# print(array_split)
# print(array_split[0])

# print('---')
# print(array_2d_0)
# print(array_2d_0.ndim, array_2d_0.shape)
# new_array_2d_0 = np.expand_dims(a = array_2d_0, axis=0)
# print(new_array_2d_0)
# print(new_array_2d_0.ndim, new_array_2d_0.shape)
# new_array_2d_0_after_squeeze = np.squeeze(new_array_2d_0)
# print(new_array_2d_0_after_squeeze)


# print('---')
# print(array_2d_0)
# print(array_2d_0.ndim, array_2d_0.shape)
# new_array_2d_0 = np.expand_dims(a = array_2d_0, axis=1)
# print(new_array_2d_0)
# print(new_array_2d_0.ndim, new_array_2d_0.shape)
# new_array_2d_0_after_squeeze = np.squeeze(new_array_2d_0)
# print(new_array_2d_0_after_squeeze)

# print("----")

# print(array_2d_0[np.newaxis, :])
# print(array_2d_0[:, np.newaxis, :])
# print(array_2d_0.reshape(3,6,1))

# print("---")
# print(array_1d)
# print(np.flip(array_1d))
# print(array_1d[::-1])

# print("---array original---")
# print(array_2d_0)
# print("---array sem axis---")
# print(np.flip(array_2d_0))

# print("--- flip axis=0---")
# print(np.flip(array_2d_0, axis=0))
# print("---flip axis=1---")
# print(np.flip(array_2d_0, axis=1))

# print("---")
# print(np.resize(a=array_2d_0, new_shape=12))
# print(np.resize(a=array_2d_0, new_shape=(2,5,3)))
# array_2d_0.reshape(2,3)

# print("---")
# print(array_1d)
# array_1d_pos_insert = np.insert(arr=array_1d, obj=4, values=-1)
# print(array_1d_pos_insert)
# array_1d_pos_insert = np.delete(arr=array_1d_pos_insert, obj=4)
# print(array_1d_pos_insert)

# print("---")
# print(array_2d_0)
# array_2d_0_pos_delete = np.delete(arr=array_2d_0, obj=0, axis=1)
# print(array_2d_0_pos_delete)

# print(array_1d)
# array_pos_append = np.append(arr=array_1d, values=[0, 1])
# print(array_pos_append)

print(array_2d_0)
array_2d_0_pos_append = np.append(arr=array_2d_0, values=[[0], [1], [2]], axis=1)
print(array_2d_0_pos_append)

print("---")
print(array_1d)
print(np.tile(A = array_1d, reps = [2,2]))

print("---")
print(array_2d_0)
print(np.tile(A = array_2d_0, reps = (2, 1)))

print("---")
array_pad = np.pad(array = array_1d, pad_width = (1,2), mode = 'constant', constant_values = (10, 20))
print(array_pad)
print("---")

array_pad = np.pad(array=array_1d, pad_width= (1, 2), mode='edge')
print(array_pad)

print("---")
array_pad = np.pad(array=array_1d, pad_width=(1, 2), mode='maximum')
print(array_pad)

array_pad = np.pad(array=array_1d, pad_width=(1, 2), mode='minimum')
print(array_pad)

array_pad = np.pad(array=array_1d, pad_width=(1, 2), mode='mean')
print(array_pad)

print('---')
print(array_2d_0)
array_pad_2d = np.pad(array=array_2d_0, pad_width=(1,2), mode='minimum')
print(array_pad_2d)

print("----")
array_with_zeros = np.pad(array=array_1d, pad_width=(1,2), mode='minimum')
print(array_with_zeros)
print(np.trim_zeros(filt=array_with_zeros))
print(np.trim_zeros(filt=array_with_zeros, trim='f'))
print(np.trim_zeros(filt=array_with_zeros, trim='b'))

print("---")
array_unique = np.array([7,8,8,6,8,7,7])
print(array_unique)
array_u, index = np.unique(ar = array_unique, return_index=True)
print(array_u)
print(index)
array_u = np.unique(ar = array_unique, return_counts = True)
print(array_u)

print("---")
print(array_2d_0)

array_unique_2d = np.array([[0,1,2],
                           [3,4,5],
                           [0,1,2]])
print(np.unique(ar = array_unique_2d, return_counts=True, axis=1))