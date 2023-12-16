import pandas as pd
import numpy as np

data = np.random.randint(1, 11, size=(10, 10))

column_names = []
for i in range(10):
    column_names.append("Col_" + str(i + 1))

df = pd.DataFrame(data, columns=column_names)

print(df)
