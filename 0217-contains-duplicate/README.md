# 217. Contains Duplicate

[LeetCode 217](https://leetcode.com/problems/contains-duplicate/) · Easy · Arrays & hashing ·
also on [NeetCode](https://neetcode.io/problems/duplicate-integer)

Given a list of integers `nums`, return `True` if any value appears at
least twice, and `False` if every element is distinct.

```
nums = [1, 2, 3, 3]  →  True
nums = [1, 2, 3, 4]  →  False
```

## Solutions

| File | Approach | Time | Space |
|---|---|---|---|
| `set_length.py` | Build a set and compare its length with the list's | O(n) | O(n) |
| `early_exit.py` | One pass with a set of seen values, return as soon as one repeats | O(n) | O(n) |

Both are O(n), but `early_exit.py` stops at the first repeated value,
so it can finish much earlier on long lists. `Counter` would also work, but
it counts every value when the question only asks whether one repeats.

## Run

```bash
python3 test_contains_duplicate.py
```
