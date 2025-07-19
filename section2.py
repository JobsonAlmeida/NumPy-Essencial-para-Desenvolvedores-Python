import numpy as np


# print(np.__version__)

# list_a = [1,2,3,4]
# print(type(list_a))

# print(id(list_a))

# list_a.append(5)
# print(list_a)
# print(id(list_a))

# array_a = np.array([1,2,3,4])
# print(type(array_a))
# print(id(array_a))
# array_a = np.append(array_a,[5])
# print(array_a)
# print(id(array_a))


# list_a = [1, 2.4, 'a' , True, 5]
# print(list_a)
# # print(type(list_a))
# # for i in list_a:
# #     print(type(i))

# array_a = np.array(list_a)
# print(array_a)
# print(type(array_a))
# for i in array_a:
#     print(type(i))
# # no array numpy para manter a homogeneidade, todos os dados são convertidos para o tipo de dados mais abrangente
# # que neste cado é o tipo string

# print(array_a.dtype)

# list_a = [1,2,3,4]
# list_b = [5,6,7,8]

# list_c = list_a + list_b

# print(list_c)


# list_c = []

# for i in range(4):
#     list_c.append(list_a[i] + list_b[i])

# print(list_c)

# array_a = np.array(list_a)
# array_b = np.array(list_b)

# array_c = array_a + array_b
# array_d = array_a - array_b
# array_e = array_a * array_b
# array_f = array_a / array_b


# print(array_c)
# print(array_d)
# print(array_e)
# print(array_f)

list_a = [1,2,3,4]
# list_a + 5

list_b = []

for i in list_a:
    list_b.append(i+5)

print(list_b)

array_a = np.array(list_a)
array_b = np.array([[5], [10]])

print(array_a + 5)
print(array_a  + array_b)

array_b = np.array([[5,6], [7,8]])

print(array_a + array_b)