from .base_strategy import AnalysisStrategy

class DailyStockStrategy(AnalysisStrategy):
    def compute(self, result, warehouse, total_days):
        filtered_stocks = [
            stock for stock, exits in zip(result.daily_stocks, result.daily_exits)
            if not (stock == 0 and exits == 0)
        ]

        avg = sum(filtered_stocks) / len(filtered_stocks) if filtered_stocks else 0

        return {"avg_stock": avg}