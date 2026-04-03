from .base_policy import RemovalPolicy

class FIFOPolicy(RemovalPolicy):
    def select_item(self, items):
        return min(items, key=lambda x: x.entry_day)