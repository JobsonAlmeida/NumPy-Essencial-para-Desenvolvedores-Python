import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# print(matplotlib.__version__)


rng = np.random.default_rng()

# print(rng.random())
# print(rng.random(size=10))
# print(rng.random(size= (5,2)))

print(rng.integers(4, size=5))
print(rng.integers(low=10, high=50, size=50))
print(rng.integers(low=10, high=[11, 60, 110]))

array = np.arange(0,10)
selected_choice = rng.choice(a = array)
selected_choice = rng.choice(a = array, size=10, replace= False)

print(selected_choice)

array = np.array([1,2,3])
p = np.array([0.5, 0.4, 0.1]) # a soma deve ser igual a 1

selected_prob = rng.choice(a=array, size=10, p=p)
print(selected_prob)

array_2d = np.arange(0,20).reshape(4,5)
print(array_2d)
array_2d_selected = rng.choice(a = array_2d, size=4, axis=0, replace=False)
print(array_2d_selected)

print("---")
print(array_2d)
array_2d_selected = rng.choice(a = array_2d, size=2, axis=1, replace=False)
print(array_2d_selected)


print("---")


array = np.arange(10)
print(array)
rng.shuffle(array)
print(array)

array = np.arange(20).reshape(4,5)
rng.shuffle(array, axis=0)
print(array)
print("---")

array = np.arange(20).reshape(4,5)
print(array)
rng.shuffle(array, axis=1)
print(array)

print("---")
array = np.arange(20).reshape(4,5)
print(array)
print(rng.permutation(array, axis=1))


print("---")
array = np.arange(20).reshape(4,5)
print(array)
print(rng.permuted(array, axis=0))

print("---")

# plt.hist(rng.beta(a=1, b=100, size=100_000), bins=100)
# # plt.show()

# print("---")
# plt.hist(rng.binomial(n=10, p=0.25, size=100_000), bins=100)
# plt.show()

print("---")

plt.hist(rng.chisquare(df=5, size=100_000), bins=100)
plt.show()


