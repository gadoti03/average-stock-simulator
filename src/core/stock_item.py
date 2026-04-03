class StockItem:
    def __init__(self, id_item, quantity, entry_day):
        self.id_item = id_item
        self.quantity = quantity
        self.entry_day = entry_day
        self.exit_day = None
    
    def duration(self):
        if self.exit_day is not None:
            return self.exit_day - self.entry_day
        return None
    
    def duration_until(self, current_day):
        return current_day - self.entry_day