import numpy as np

class Product:
    def __init__(self, id, name, price, category):
        self.id, self.name, self.price, self.category = id, name, price, category
    def __repr__(self):
        return f"Product({self.id}, '{self.name}', {self.price}, '{self.category}')"

products = [Product(1,"Laptop",1200.0,"Electronics"), Product(2,"Mouse",25.0,"Electronics"), Product(3,"Monitor",450.0,"Electronics")]
prices = np.array([p.price for p in products])

mean_p = np.mean(prices)
result = [p for p in products if p.price > mean_p]
print(result)