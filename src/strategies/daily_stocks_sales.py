from .base_strategy import AnalysisStrategy

class DailyStockStrategy(AnalysisStrategy):
    def compute(self, result, warehouse, total_days):
        avg = sum(result.daily_stocks) / len(result.daily_stocks)
        return {"avg_stock": avg}