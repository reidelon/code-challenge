"""Run every Contains Duplicate solution against the same cases.

    python3 0217-contains-duplicate/test_contains_duplicate.py
"""

import early_exit
import set_length

SOLUTIONS = [set_length, early_exit]

CASES = [
    ([1, 2, 3, 3], True),
    ([1, 2, 3, 4], False),
    # edge cases
    ([], False),                        # empty list
    ([7], False),                       # single element
    ([1, 1], True),                     # only a duplicate pair
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),  # many duplicates
    ([5, 2, 9, 4, 5], True),            # duplicate far apart
    ([-1, 0, 1, -1], True),             # negatives
    (list(range(10000)), False),        # long list, all distinct
]


if __name__ == "__main__":
    for solution in SOLUTIONS:
        print(f"== {solution.__name__}")
        for nums, expected in CASES:
            result = solution.contains_duplicate(nums)
            ok = result == expected
            shown = nums if len(nums) <= 12 else f"[{len(nums)} items]"
            print("OK  " if ok else "FAIL", shown, "->", result, "(expected", expected, ")")
