import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('emojis.csv')

df['Year'] = pd.to_datetime(df['Year'])

emojis_per_year = df.groupby('Year').size()

emojis_per_year.plot(kind='bar')
plt.xlabel('Год')
plt.ylabel('Количество эмоджи')
plt.title('Количество эмоджи по годам')
plt.show()
