"""Run every Valid Anagram solution against the same cases.

    python3 0242-valid-anagram/test_valid_anagram.py
"""

import counter
import dict_count
import manual_count
import sorted_compare

SOLUTIONS = [counter, sorted_compare, manual_count, dict_count]

CASES = [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    # edge cases
    ("", "", True),                 # both empty
    ("a", "a", True),               # single letter
    ("a", "ab", False),             # different lengths
    ("aacc", "ccac", False),        # same letters, different counts
    ("listen", "silent", True),
    ("ab", "ba", True),
    ("a" * 5000 + "b", "b" + "a" * 5000, True),  # long strings
]


if __name__ == "__main__":
    for solution in SOLUTIONS:
        print(f"== {solution.__name__}")
        for s, t, expected in CASES:
            result = solution.is_anagram(s, t)
            ok = result == expected
            shown = (s, t) if len(s) <= 12 else f"[{len(s)} chars]"
            print("OK  " if ok else "FAIL", shown, "->", result, "(expected", expected, ")")
