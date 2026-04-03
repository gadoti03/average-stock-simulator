from .base_policy import RemovalPolicy

class FILOPolicy(RemovalPolicy):
    def select_item(self, items):
        return max(items, key=lambda x: x.entry_day)