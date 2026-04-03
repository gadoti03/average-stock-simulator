class Simulator:
    def __init__(self, warehouse, policy):
        self.warehouse = warehouse
        self.policy = policy

    def process_day(self, day, entries, exits):
        for entry in entries:
            self.warehouse.add_item(entry)

        for _ in range(exits):
            if self.warehouse.current_items:
                item = self.policy.select_item(self.warehouse.current_items)
                self.warehouse.remove_item(item, exit_day=day)