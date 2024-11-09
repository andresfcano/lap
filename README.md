# Linear Assignment Problem

## Prerequisites

- A reasonably recent version of Python (3.x)
- NumPy installed (`pip install numpy`)

## LAP Solvers

### LAP Solver: `lap.py`
Uses the Sinkhorn algorithm. 

`>> python3 lap.py cost.dat`

### Brute Force Solver: `all_permutations.py`
Identifies the assignment with the maximum total cost by iterating through all permutations and comparing their costs. While comprehensive, this approach is computationally expensive, making it practical only for small matrices due to its factorial time complexity.

`>> python3 all_permutations.py cost.dat`

# Performance Comparison

The Python script (`lap_loop.py`) generates random n x n  cost matrices where `n ∈ {9, 10, 11, 12}`, and runs the `lap.py` Linear Assignment Problem (LAP) solver to get the average solving time over 100 iterations.

## Summary of Results

| Script                 | Algorithm Used        | Complexity           | Practical Usage              | Average Time (n=12) |
|-------------------------|-----------------------|-----------------------|------------------------------|----------------------|
| `lap.py`               | Sinkhorn Algorithm    | O(k * n^2)           | Efficient for large n        | 0.1578 seconds       |
| `all_permutations.py` | Brute-force Permutations | O(n! * n)            | Feasible only for small n    | Memory Error         |

---

### Average Solving Time for Different `n`

| Matrix Size (n) | Sinkhorn (seconds) | All Permutations (seconds) |
|------------------|--------------------------------|------------------------------------------|
| 9                | 0.1234                         | 1.94                                     |
| 10               | 0.1356                         | 21.89                                    |
| 11               | 0.1457                         | 243.21                                   |
| 12               | 0.1578                         | Memory error!                            |


## Notes
1. Ensure `lap.py` is in the same directory as this script.
2. The generated matrix is saved in `cost.dat` (space-separated format).
3. Modify `sizes`, `iterations`, or `gamma` to customize tests.
