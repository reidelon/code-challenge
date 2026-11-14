# 1. Two Sum

[LeetCode 1](https://leetcode.com/problems/two-sum/) · Easy · Arrays & hashing

Given a list of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to `target`. There is exactly one valid
answer, and the same element can't be used twice. Any order is accepted.

```
nums = [2, 7, 11, 15], target = 9  →  [0, 1]
```

## Solutions

| File | Approach | Time | Space |
|---|---|---|---|
| `brute_force.py` | Try every pair of indices | O(n²) | O(1) |
| `one_pass.py` | One pass, look up `target - value` in a dict of values already seen | O(n) | O(n) |

The brute force was the first idea that worked. The dict version trades
memory for speed: doubling the list doubles the work instead of making it
four times bigger.

## Run

```bash
python3 test_two_sum.py
```
