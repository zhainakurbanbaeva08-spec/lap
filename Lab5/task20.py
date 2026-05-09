totals = np.array([1200.0, 900.0, 1500.0])
indices = np.where(totals > 1000)[0]
print("Задача 20:", indices.tolist())