"""Contains Duplicate — one pass with a set, stopping early.

Walk the list keeping a set of values already seen. If the current value
is already in the set, there is a duplicate: stop and return True.
Otherwise add it and keep going.

Complexity: O(n) time, O(n) extra space in the worst case (no duplicates),
but it stops as soon as it finds the first repeated value.
"""


def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
