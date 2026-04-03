class Warehouse:
    def __init__(self):
        self.current_items = []
        self.past_items = []

    def add_item(self, stock_item):
        self.current_items.append(stock_item)

    def remove_item(self, stock_item, exit_day):
        stock_item.exit_day = exit_day
        self.current_items.remove(stock_item)
        self.past_items.append(stock_item)