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

    def __str__(self):
        return f"Цена {self.name}: {self.price}"


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    @property
    def discount_price(self):
        return self.price * (1 - self.discount / 100)

    def __str__(self):
        (1 - self.discount / 100)
        return f"Цена {self.name} со скидкой {self.discount}% : {self.discount_price}"

    def get_parent_data(self):
        return f"item: {self.name}, price: {self.price}"


if __name__ == "__main__":
    item_parent = ItemDiscount("Процессор", 5000)
    print(item_parent)

    item = ItemDiscountReport("Монитор", 15000, 20)
    print(item)