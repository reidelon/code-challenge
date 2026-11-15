# Code challenges

Classic interview problems solved in Python, without AI help and against the clock.
Each problem has its own folder with every approach I tried, from the first
one that worked to the optimized one, all checked by the same test cases.
Problems with no LeetCode number (`—`) are ones I was given in live-coding
interviews, redone calmly afterwards.

## Problems

| # | Problem | Pattern | Solutions |
|---|---|---|---|
| 1 | [Two Sum](0001-two-sum/) | Arrays & hashing | Brute force O(n²) · One pass with a dict O(n) |
| 217 | [Contains Duplicate](0217-contains-duplicate/) | Arrays & hashing | Set length O(n) · One pass with early exit O(n) |
| 242 | [Valid Anagram](0242-valid-anagram/) | Arrays & hashing | Counter O(n) · Sort O(n log n) · Set + count O(k·n) · Dict count O(n) |
| — | [Print a 2D array in zigzag](zigzag-matrix/) | Matrices / traversal | Rows with `[::-1]` on odd indexes O(R×C) |

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
