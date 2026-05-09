import numpy as np
def get_price_stats(prices_array):
    mean_price = np.mean(prices_array)
    median_price = np.median(prices_array)
    return (mean_price, median_price)

prices = np.array([1200.0, 25.0, 450.0])
print(get_price_stats(prices))