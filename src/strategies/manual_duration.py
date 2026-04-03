from .base_strategy import AnalysisStrategy

class ManualDurationStrategy(AnalysisStrategy):
    def compute(self, result, warehouse, total_days):
        total_duration = 0
        total_items = 0

        for item in warehouse.past_items:
            total_duration += item.duration()
            total_items += 1

        for item in warehouse.current_items:
            total_duration += item.duration_until(total_days)
            total_items += 1

        avg_duration = total_duration / total_items if total_items else 0

        return {
            "avg_duration_manual": avg_duration
        }