import numpy as np
def count_unique_categories(categories_array):
    unique_cats = np.unique(categories_array)
    return len(unique_cats)

cats = np.array(["Electronics", "Clothing", "Electronics"])
print(count_unique_categories(cats))