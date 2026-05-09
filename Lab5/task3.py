class Product:
    def __init__(self, product_id, name, price, category):
        self.id = product_id
        self.name = name
        self.price = float(price)
        self.category = category

    def __str__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price}, category='{self.category}')"

    def __eq__(self, other):
        return isinstance(other, Product) and self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'price': self.price, 'category': self.category}

p = Product(1, 'Laptop', 1200.0, 'Electronics')
print(p)
print(p.to_dict())