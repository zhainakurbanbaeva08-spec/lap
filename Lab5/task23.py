orders_df = pd.DataFrame({'order_id': [101, 102], 'user_id': [1, 2], 'total': [1200, 25]})
merged_df = pd.merge(users_df, orders_df, left_on='id', right_on='user_id')
result = merged_df[['order_id', 'name', 'total']].rename(columns={'name': 'user_name'})
print("Задача 23:\n", result)