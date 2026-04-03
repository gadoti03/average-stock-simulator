from src.results.simulation_result import SimulationResult

class Simulator:
    def __init__(self, warehouse, policy):
        self.warehouse = warehouse
        self.policy = policy
        self.result = SimulationResult()

    def process_day(self, day, entries, exits):
        # salva entries
        self.result.daily_entries.append(len(entries))
        self.result.total_entries += len(entries)

        # aggiungi entries
        for item in entries:
            self.warehouse.add_item(item)

        # gestisci exits
        sold_today = 0
        for _ in range(exits):
            if self.warehouse.current_items:
                item = self.policy.select_item(self.warehouse.current_items)
                self.warehouse.remove_item(item, exit_day=day)
                sold_today += 1

        self.result.daily_exits.append(sold_today)
        self.result.total_exits += sold_today

        # stock a fine giornata
        self.result.daily_stocks.append(len(self.warehouse.current_items))

    def get_result(self):
        return self.result