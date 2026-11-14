"""Contains Duplicate — compare lengths with a set.

A set drops repeated values, so if it ends up shorter than the list,
some value appeared more than once.

Complexity: O(n) time, O(n) extra space. It always builds the whole set,
even when the duplicate is at the start.
"""


def contains_duplicate(nums: list[int]) -> bool:
    return len(set(nums)) != len(nums)
