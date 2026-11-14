"""Two Sum — one pass with a dict.

Walk the list once. For each value, compute the number still needed
(`target - value`) and check whether it was already seen. If so, return both
indices; if not, store the value with its index. Checking before storing
keeps an element from pairing with itself.

Complexity: O(n) time (one pass, dict lookups are O(1) on average),
O(n) extra space (the dict can hold almost every value).
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}  # value -> index
    for index, value in enumerate(nums):
        diff = target - value
        if diff in seen:
            return [seen[diff], index]
        seen[value] = index
