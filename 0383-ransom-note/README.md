# 383. Ransom Note

[LeetCode 383](https://leetcode.com/problems/ransom-note/) · Easy · Arrays & hashing

Given two strings `ransomNote` and `magazine`, return `True` if `ransomNote`
can be built with the letters of `magazine`, using each letter only once.

```
ransomNote = "a",  magazine = "b"    →  False
ransomNote = "aa", magazine = "ab"   →  False
ransomNote = "aa", magazine = "aab"  →  True
```

## Solutions

| File | Approach | Time | Space |
|---|---|---|---|
| `counter.py` | Count both strings with `Counter`; fail as soon as a letter of the note appears more times than in the magazine | O(n + m) | O(1) |

## Run

```bash
python3 0383-ransom-note/test_ransom_note.py
```
