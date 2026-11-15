# Print a 2D array in zigzag

Real interview challenge · fintech company · Oct 2025 · Matrices / traversal

Print a 2D array in zigzag pattern. Even rows (0, 2, 4...) are printed left
to right. Odd rows (1, 3, 5...) are printed right to left.

```
[[1, 2, 3, 4],
 [5, 6, 7, 8],      →  1, 2, 3, 4, 8, 7, 6, 5, 9, 10, 11, 12
 [9, 10, 11, 12]]
```

Key point: the direction depends on the **row index**, not on the values.

## Solutions

| File | Approach | Time | Space |
|---|---|---|---|
| `zigzag.py` | Walk the rows; odd row index → add it reversed with `[::-1]` (a copy, the input is not mutated) | O(R×C) | O(R×C) for the output |

`R` = rows, `C` = columns: every value is visited once.

## Run

```bash
python3 test_zigzag.py
```
