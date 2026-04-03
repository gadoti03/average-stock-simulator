import random
from src.core.stock_item import StockItem

class EventGenerator:
    def __init__(self, max_daily_entries=5, max_daily_exits=5, seed=None):
        self.max_daily_entries = max_daily_entries
        self.max_daily_exits = max_daily_exits
        self.current_stock = 0
        self.next_id = 1

        # Seed random
        self.random = random.Random(seed)

    def generate_day(self, day):
        num_entries = self.random.randint(0, self.max_daily_entries)
        entries = []

        for _ in range(num_entries):
            item = StockItem(
                id_item=self.next_id,
                quantity=1,
                entry_day=day
            )
            entries.append(item)
            self.next_id += 1

        self.current_stock += num_entries

        max_possible_exits = min(self.current_stock, self.max_daily_exits)
        num_exits = self.random.randint(0, max_possible_exits)

        self.current_stock -= num_exits

        return entries, num_exits