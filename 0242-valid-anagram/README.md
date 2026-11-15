# 242. Valid Anagram

[LeetCode 242](https://leetcode.com/problems/valid-anagram/) · Easy · Arrays & hashing ·
also on [NeetCode](https://neetcode.io/problems/is-anagram)

Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`:
the same letters, each one the same number of times.

```
s = "anagram", t = "nagaram"  →  True
s = "rat",     t = "car"      →  False
```

## Solutions

| File | Approach | Time | Space |
|---|---|---|---|
| `counter.py` | Count letters of both strings with `Counter` and compare | O(n + m) | O(k) |
| `sorted_compare.py` | Sort both strings and compare | O(n log n) | O(n) |
| `manual_count.py` | Set of seen letters + `str.count` for each one | O(k·n) | O(k) |
| `dict_count.py` | Dict letter → count: +1 for `s`, −1 for `t`, all must end at 0 | O(n) | O(k) |

`k` = number of distinct letters.

`dict_count.py` is the one to give when asked "without Counter": O(n) for any
characters. `manual_count.py` is O(n) only because the alphabet is small (26 letters).

## Run

```bash
python3 test_valid_anagram.py
```
