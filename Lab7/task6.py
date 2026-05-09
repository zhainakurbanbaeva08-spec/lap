df_encoded = pd.get_dummies(df, columns=['col_7'], drop_first=True)

print("Категории закодированы. Теперь столбцов в таблице:", df_encoded.shape[1])