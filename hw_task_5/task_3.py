import pandas as pd
import numpy as np

data = np.random.randint(1, 101, size=(10, 10))

columns = list('ABCDEFGHIJ')
index = list('abcdefghij')

df = pd.DataFrame(data, columns=columns, index=index)

print("Размерность матрицы:", df.shape)
print("\nИндексы столбцов:", df.columns)
print("\nСреднее значение всех чисел матрицы:", df.values.mean())

df.to_csv("random_matrix.csv", index_label="Index")

print("\nDataFrame:")
print(df)
