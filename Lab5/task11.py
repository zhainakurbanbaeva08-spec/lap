import numpy as np
def get_categories_array(products):
    return np.array([p.category for p in products])

products = [Product(1, "Laptop", 1200.0, "Electronics"), Product(2, "T-Shirt", 20.0, "Clothing")]
categories = get_categories_array(products)
print(categories)