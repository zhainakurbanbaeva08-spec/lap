umeric_cols = df.select_dtypes(include=['number']).columns
df[numeric_cols] = df[numeric_cols].astype(float)

df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

df.dropna(inplace=True)

print("Данные очищены. Текущее количество строк:", len(df))