import numpy as np
def normalize_prices(prices_array):
    p_min = np.min(prices_array)
    p_max = np.max(prices_array)
    return (prices_array - p_min) / (p_max - p_min)

prices = np.array([1200.0, 25.0, 450.0])
print(normalize_prices(prices))