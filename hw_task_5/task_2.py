import pandas as pd
import numpy as np

data = np.random.randint(1, 11, size=(10, 10))

column_names = [f"Col_{i}" for i in range(10)]

df = pd.DataFrame(data, columns=column_names, index=list('ABCDEFGHIJ'))

print("DataFrame с индексами в виде латинских букв:")
print(df)

filtered_row = df[(df > 5).all(axis=1)]
if not filtered_row.empty:
    print("\nСтрока, в которой все числа больше 5:")
    print(filtered_row)
else:
    print("\nСтрока, в которой все числа больше 5 отсутствует.")
