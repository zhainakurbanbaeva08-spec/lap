class Order:
    def __init__(self, order_id, user, products=None):
        self.id = order_id
        self.user = user
        self.products = products or []

    def add_product(self, product):
        self.products.append(product)
    def total_price(self):
        return sum(p.price for p in self.products)
    def most_expensive_products(self, n):
        return sorted(self.products, key=lambda p: p.price, reverse=True)[:n]
    def __str__(self):
        return f"Order {self.id}, Total: {self.total_price()}"


o = Order(1, "UserObj")
o.add_product(Product(1, "A", 10.0, "C"))
o.add_product(Product(2, "B", 50.0, "C"))
print(o)
print(o.most_expensive_products(1)[0].name)