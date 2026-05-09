class Inventory:
    def __init__(self):
        self._products={}
    def add_product(self,product):
        if product.id not in self._products:
            self._products[product.id]=product

    def remove_product(self, product_id):
        self._products.pop(product_id, None)
    def get_all_products(self):
        return list(self._products.values())
    def filter_by_price(self, min_price):
        check=lambda p: p.price>=min_price
        return [p for p in self.get_all_products() if check(p)]

inv=Inventory()
expensive=inv.filter_by_price(100)
inv.add_product(Product(1, "Laptop", 2000, "Electronics"))
inv.add_product(Product(2, "Mouse", 100,"Electronics"))
inv.add_product(Product(3, "Phone", 1100,"Electronics"))
inv.add_product(Product(4, "Monitor", 5100,"Electronics"))
print([p.name for p in expensive])