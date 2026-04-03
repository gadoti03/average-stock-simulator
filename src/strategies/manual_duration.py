from .base_strategy import AnalysisStrategy

class ManualDurationStrategy(AnalysisStrategy):
    def compute(self, result, warehouse, total_days):
        total_duration = 0

        for item in warehouse.past_items:
            total_duration += item.duration()

        for item in warehouse.current_items:
            total_duration += item.duration_until(total_days)

        avg = total_duration / total_days if total_days else 0

        return {
            "avg_stock_manual": avg
        }