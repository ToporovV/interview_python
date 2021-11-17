class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f"item: {self.__name}, price: {self.__price}"


if __name__ == "__main__":
    item = ItemDiscountReport("Монитор", 15000)
    try:
        print(item.get_parent_data())
    except AttributeError as err:
        print(f"method get_parent_data error: {err}, {type(item)}")