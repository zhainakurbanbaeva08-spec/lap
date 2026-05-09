import numpy as np

def get_prices_array(products):
    return np.array([p.price for p in products], dtype=float)

products = [Product(1, "Laptop", 1200.0, "Tech"), Product(2, "Mouse", 25.0, "Tech")]
prices = get_prices_array(products)
print(prices)