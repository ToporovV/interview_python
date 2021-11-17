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
        return f"Price for {self.name}: {self.price}"


class ItemDiscountReportName(ItemDiscount):
    def get_info(self):
        return f"Наименование {self.name}"


class ItemDiscountReportPrice(ItemDiscount):
    def get_info(self):
        return f"Цена {self.price}"


if __name__ == "__main__":
    item_name = ItemDiscountReportName("Процессор", 5000)
    print(item_name.get_info())

    item_price = ItemDiscountReportPrice("Монитор", 15000)
    print(item_price.get_info())