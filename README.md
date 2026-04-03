# Average Stock Simulator

This repository contains a **simulator for calculating the average stock** of a product in a warehouse, based solely on purchase and sales orders and their respective quantities.

The main goal is to **test the validity of the formula**:

```
average stock / average number of sales = sum of daily stocks / total sales
```

for calculating the **average duration of stock** of a product in the warehouse.

---

## Main Features

* Simulates product extraction according to different **warehouse policies**:

  * **FIFO** (First In, First Out)
  * **LIFO** (Last In, First Out)
  * **Random**

* Compares two methods for calculating average stock duration:

### 1. Manual Calculation (`src/strategies/manual_duration.py`)

* Implements the **correct calculation** manually.
* Each product is extracted according to the selected policy (FIFO/LIFO/Random) during sales.
* The **duration of each item in stock** is calculated individually.
* The average duration is obtained by summing all durations and dividing by the **total number of sold items**.

### 2. Formula-based Calculation (`src/strategies/daily_stocks_sales.py`)

* Uses the **formula being tested**: sum of daily stocks divided by total sales.
* Calculates average stock duration using only:

  * days with sales
  * or days when stock is greater than zero

---

## Repository Structure

```
src/
├── core/
│   ├── simulator.py
│   ├── warehouse.py
│   └── stock_item.py
├── policies/
│   ├── base_policy.py
│   ├── fifo.py
│   ├── filo.py
│   └── random_policy.py
├── strategies/
│   ├── base_strategy.py
│   ├── manual_duration.py
│   └── daily_stocks_sales.py
├── results/
│   └── simulation_result.py
└── utils.py
```

---

## How to Run the Simulator

Run the `main.py` script with the CLI arguments:

```bash
python main.py --policy fifo --days 10 --seed 42
```

CLI arguments:

```python
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
```

---

## Notes

* `simulation_result.py` is used to **store simulation results**.
* The simulator allows comparing the **manual correct calculation** versus the **formula-based approach** for evaluating average stock duration.
