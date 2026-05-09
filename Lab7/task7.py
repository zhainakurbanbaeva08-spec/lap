from sklearn.model_selection import train_test_split

y = df_encoded['col_2']

X = df_encoded.drop(['col_2', 'log_price', 'total_value'], axis=1)
X = X.select_dtypes(include=[np.number])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Размер обучающей выборки: {X_train.shape[0]}")
print(f"Размер тестовой выборки: {X_test.shape[0]}")