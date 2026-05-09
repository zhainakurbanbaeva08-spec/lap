class OrderIterator:
    def __init__(self, orders):
        self._orders = orders
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._orders):
            raise StopIteration
        res = self._orders[self._index]
        self._index += 1
        return res

o = ["Order1", "Order2", "Order3"]
it = OrderIterator(orders)
for o in it:
    print(o)