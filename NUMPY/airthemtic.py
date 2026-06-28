import numpy as np

# Scaler Airthemtic 

array = np.array([1, 2, 3])
# print(array + 1)
# print(array - 2)
# print(array * 3)
# print(array / 4)
# print(array ** 5)

# Vectorized math funcs

array = np.array([1, 2, 3])
print(np.sqrt(array))
print(np.round(array)) 
print(np.pi)


#exercise

radii = np.array([1, 2, 3])

print(np.pi * radii ** 2)


# Eliment wise arithmetic 

# array1 = np.array([1, 2, 3])
# array2 = np.array([4, 5, 6])

# print(array1 + array2)
# print(array1 - array2)
# print(array1 * array2)
# print(array1 / array2)


# Comparison operators 

score = np.array([91, 55, 100, 73, 82, 64])

print(score < 60)

score[score < 60] = 0
print(score)