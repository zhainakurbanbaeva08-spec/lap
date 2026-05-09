import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
sns.histplot(df['col_2'], bins=30, color='skyblue')
plt.title('Распределение цены')

plt.subplot(1, 3, 2)
sns.scatterplot(x=df['col_3'], y=df['col_2'], alpha=0.5)
plt.title('Цена vs Количество')

plt.subplot(1, 3, 3)
sns.boxplot(x='col_7', y='col_2', data=df)
plt.xticks(rotation=45)
plt.title('Цена по категориям')

plt.tight_layout()
plt.show()