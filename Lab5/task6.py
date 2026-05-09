ef price_stream(products):
    for product in products:
        yield product.price

products_list = [Product(1, "A", 10.0, "C"), Product(2, "B", 20.0, "C")]
for price in price_stream(products_list):
    print(price)