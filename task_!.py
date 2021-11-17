class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f"item: {self.name}, price: {self.price}"


if __name__ == "__main__":
    item = ItemDiscount("Монитор", 15000)
    try:
        print(item.get_parent_data())
    except AttributeError as err:
        print(f"method get_parent_data error: {err}, {type(item)}")

    item_report = ItemDiscountReport("Процессор", 5000)
    print(item_report.get_parent_data())