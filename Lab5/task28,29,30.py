print("Задача 28:\n", products_df.groupby('category')['price'].mean())

products_df['discounted_price'] = products_df['price'] * 0.9
print("\nЗадача 29:\n", products_df)

sorted_df = products_df.sort_values(by='price', ascending=False)
print("\nЗадача 30:\n", sorted_df)