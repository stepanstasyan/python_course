import numpy as np

height = 5
width = 3

vector = np.zeros(height * width)

if width % 2 == 0:

    for index, value in enumerate(vector):
        if index % 2 == 0:
            vector[index] = 1.0
    matrix = vector.reshape(height, width)
    for index, value in enumerate(matrix):
        if index % 2 == 0:
            matrix[index] = matrix[index][::-1]

else:
    for index, value in enumerate(vector):
        if index % 2 == 0:
            vector[index] = 1.0
    matrix = vector.reshape(height, width)

print(matrix)

