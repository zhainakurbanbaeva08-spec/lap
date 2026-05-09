ean = df['col_2'].mean()
std = df['col_2'].std()

upper_limit = mean + 3 * std
lower_limit = mean - 3 * std

anomalies = df[(df['col_2'] > upper_limit) | (df['col_2'] < lower_limit)]

df = df[(df['col_2'] >= lower_limit) & (df['col_2'] <= upper_limit)]

print(f"Найдено аномалий: {len(anomalies)}")
print(f"Осталось данных для обучения: {len(df)}")