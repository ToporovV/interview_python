class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f"item: {self.name}, price: {self.price}"


if __name__ == "__main__":
    item = ItemDiscountReport("Монитор", 15000)
    item.price = 20000

    print(item.get_parent_data())
    print(f"Parent price value: {item._ItemDiscount__price}")