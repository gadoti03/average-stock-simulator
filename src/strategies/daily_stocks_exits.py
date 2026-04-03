from .base_strategy import AnalysisStrategy

class DailyStockStrategy(AnalysisStrategy):
    def compute(self, result, warehouse, total_days):
        # Filter out days with zero stock and zero exits to avoid skewing the average
        filtered = [
            (stock, exits) 
            for stock, exits in zip(result.daily_stocks, result.daily_exits) 
            if not (stock == 0 and exits == 0)
        ]

        total_stock_days = sum(stock for stock, _ in filtered)
        total_exits = sum(exits for _, exits in filtered)

        avg_duration = total_stock_days / total_exits if total_exits else 0

        return {"avg_duration": avg_duration}