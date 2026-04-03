from abc import ABC, abstractmethod

class AnalysisStrategy(ABC):
    @abstractmethod
    def compute(self, result, warehouse, total_days):
        pass