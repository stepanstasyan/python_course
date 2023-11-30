import numpy as np

# заполнение случайными занчениями от 0 до 1:
vector = np.random.uniform(0, 1, size=10)
# in random.uniform samples are uniformly distributed over the half-open interval [low, high)
# vector = np.random.random_sample(10) - return random floats in the half-open interval [0.0, 1.0)

while 0 in vector:
    vector = np.random.uniform(0, 1, size=10)
    break

print(vector)



# заполнение с равными промежутками:
N = 10
vector_2 = np.linspace(0, 1, N+2)[1:-1]
print(vector_2)
