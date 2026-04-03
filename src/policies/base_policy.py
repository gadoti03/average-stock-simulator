from abc import ABC, abstractmethod

class RemovalPolicy(ABC):
    @abstractmethod
    def select_item(self, items):
        pass