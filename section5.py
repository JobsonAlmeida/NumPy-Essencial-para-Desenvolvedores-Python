import numpy as np

list_3d = [[ [1,2,3],
             [4,5,6],
             [7,8,9],
             [10,11,12]],
            
            [[13,14,15],
             [16,17,18],
             [19,20,21],
             [22,23,24]]]

array_3d = np.array(list_3d)
print(array_3d)
print(array_3d.shape)
print("----")

print(array_3d[0, 1])
print(array_3d[[0, 1]])

print("---fancy indexing---")
# print(array_3d[[0,1,1], [[0,1],0,1], :])

print(array_3d[-1, -2, -2])

mask = [True, False]

print("---")
print(array_3d[mask])


mask = array_3d   %2 == 0
print(mask)

print(array_3d[mask])

print("---slicing---")

list_3d = [[ [1,2,3],
             [4,5,6],
             [7,8,9],
             [10,11,12]],
            
            [[13,14,15],
             [16,17,18],
             [19,20,21],
             [22,23,24]]]


print(array_3d[0:2, 1:3])

print("---")
print(array_3d[:, 1:3, -1])


print("---")
print(array_3d[0, 1:4:2])


print("---")
print(array_3d[0, ::2])

print("---")
print(array_3d[0, ::-2])


print("---")
print(array_3d[0, ::-1])

list_3d = [[ [1,2,3],
             [4,5,6],
             [7,8,9],
             [10,11,12]],
            
            [[13,14,15],
             [16,17,18],
             [19,20,21],
             [22,23,24]]]

print("---")
print(array_3d[1][2][0])
print(array_3d[1, 2, 0])

# array_3d[1,2,0] = 50

print(array_3d[1, 2, 0])

print("---")
print(array_3d[:, 1:3, :-1 ])

array_3d[:, 1:3, :-1 ] = [[[64, 65],
                           [67, 68]],
                           
                           [[76, 77],
                            [78, 80]]]

print("--")
print(array_3d)
array_3d[0] = 99
print(array_3d)


