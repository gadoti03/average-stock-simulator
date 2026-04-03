import random
from .base_policy import RemovalPolicy

class RandomPolicy(RemovalPolicy):
    def select_item(self, items):
        return random.choice(items)