import pandas as pd

df = pd.read_csv('emojis.csv')

df_sorted = df.sort_values(by='Rank', ascending=True)

most_popular_category = df_sorted['Subcategory'].iat[0]
print(f"Самая популярная подкатегория эмоджи: {most_popular_category}")

