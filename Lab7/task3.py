import numpy as np

df['total_value'] = df['col_2'] * df['col_3']

df['log_price'] = np.log1p(df['col_2'])

df['double_stock'] = df['col_3'] * 2

print("Новые признаки добавлены успешно.")