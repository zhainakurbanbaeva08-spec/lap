import pandas as pd

df = pd.read_csv('catalog_products.xlsx - Sheet1.csv')

print("--- Первые 5 строк таблицы ---")
print(df.head())

print(f"\nФорма DataFrame: {df.shape}")

print("\n--- Типы данных ---")
print(df.dtypes)

print("\n--- Количество пропусков ---")
print(df.isnull().sum())