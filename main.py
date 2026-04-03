import argparse

from src.warehouse import Warehouse
from src.simulator import Simulator
from src.policies.fifo import FIFOPolicy
from src.policies.filo import FILOPolicy
from src.policies.random_policy import RandomPolicy
from src.utils import EventGenerator
from src.strategies.daily_stocks_exits import DailyStockStrategy
from src.strategies.manual_duration import ManualDurationStrategy


def get_policy(name):
    name = name.lower()
    if name == "fifo":
        return FIFOPolicy()
    elif name == "filo":
        return FILOPolicy()
    elif name == "random":
        return RandomPolicy()
    else:
        raise ValueError(f"Unknown policy: {name}")


def main():
    # Parser CLI (Command Line Interface)
    parser = argparse.ArgumentParser(description="Average Stock Simulator")
    parser.add_argument(
        "--policy",
        type=str,
        required=True,
        help="Policy to use: fifo | filo | random"
    )
    parser.add_argument(
        "--days",
        type=int,
        default=10,
        help="Number of simulation days"
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for reproducibility"
    )

    args = parser.parse_args()

    # select policy
    policy = get_policy(args.policy)

    warehouse = Warehouse()
    simulator = Simulator(warehouse, policy)
    generator = EventGenerator(seed=args.seed)


    for day in range(1, args.days + 1):
        entries, exits = generator.generate_day(day)
        simulator.process_day(day, entries, exits)

    result = simulator.get_result()

    # print(result.daily_entries)
    # print(result.daily_exits)
    # print(result.daily_stocks)
    # print(result.total_entries)
    # print(result.total_exits)

    daily_strategy = DailyStockStrategy()
    manual_strategy = ManualDurationStrategy()

    daily_report = daily_strategy.compute(result, warehouse, args.days)
    manual_report = manual_strategy.compute(result, warehouse, args.days)

    print(daily_report)
    print(manual_report)

if __name__ == "__main__":
    main()