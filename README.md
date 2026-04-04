# Average Stock Time Simulator

This repository contains a **simulator for calculating the average stock time** of a product in a warehouse, based solely on purchase and sales orders and their respective quantities.

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

To run the simulator, execute the `main.py` script and specify the following parameters:

* **Policy** `<--policy>`: Choose the stock extraction method:

  * `fifo`  → First In, First Out
  * `filo`  → Last In, First Out
  * `random` → Random selection of items

* **Number of simulation days** `<--days>`: Define how many days the simulation should run. Only affects the length of the simulated timeline.

* **Random seed** `<--seed>`: Optional parameter to ensure reproducibility when using the random policy. Same seed produces the same results across runs.

Example usage:

```
python main.py --policy fifo --days 10 --seed 42
```

This will run the simulator using the FIFO policy for 10 days with a fixed random seed for reproducibility.

---

## Notes

* `simulation_result.py` is used to **store simulation results**.
* The simulator allows comparing the **manual correct calculation** versus the **formula-based approach** for evaluating average stock duration.
