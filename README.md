# Average Stock Simulator

This repository contains a **simulator for calculating the average stock** of a product in a warehouse, based solely on purchase and sales orders and their respective quantities.

---

## Main Features

* Simulates product extraction according to different **warehouse policies**:

  * **FIFO** (First In, First Out)
  * **LIFO** (Last In, First Out)
  * **Random**

* Compares two methods for calculating average stock:

### 1. Manual Calculation (`src/strategies/manual_duration.py`)

* Each product is extracted according to the selected policy (FIFO/LIFO/Random) during sales.
* The **duration of each item in stock** is calculated.
* The average stock is obtained by summing all durations and dividing by the **total number of sold items**.

### 2. Daily Stock Ratio Calculation (`src/strategies/daily_stocks_sales.py`)

* Calculates average stock using the ratio between **average stock** and **average duration**, considering only:

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

## How to Use the Simulator

1. Install dependencies (if any).
2. Run the main script (e.g., `main.py`) specifying the desired policy and input data.
3. Compare results between **manual calculation** and **daily ratio calculation**.

---

## Notes

* `simulation_result.py` is used to **store simulation results**.
* The implemented strategies allow evaluating how the warehouse policy affects the calculation of average stock.
