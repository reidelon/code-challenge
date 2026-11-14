# Code challenges

Classic interview problems solved in Python, without AI help and against the clock.
Each problem has its own folder with every approach I tried, from the first
one that worked to the optimized one, all checked by the same test cases.

## Problems

| # | Problem | Pattern | Solutions |
|---|---|---|---|
| 1 | [Two Sum](0001-two-sum/) | Arrays & hashing | Brute force O(n²) · One pass with a dict O(n) |
| 217 | [Contains Duplicate](0217-contains-duplicate/) | Arrays & hashing | Set length O(n) · One pass with early exit O(n) |

## Layout

```
NNNN-problem-name/
├── README.md          # problem statement + table of approaches
├── <approach>.py      # one file per approach, each exposes the same function
└── test_<problem>.py  # runs every approach against the same cases
```

## Run

Requires Python 3.9+ (no dependencies).

```bash
python3 0001-two-sum/test_two_sum.py
```

Each case prints `OK` or `FAIL` with the result and the expected answer.
