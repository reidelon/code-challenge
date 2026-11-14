"""Two Sum — brute force.

Try every pair of indices until one adds up to `target`.

Complexity: O(n^2) time (it checks every pair), O(1) extra space
(`itertools.combinations` yields the pairs one at a time).
"""

import itertools


def two_sum(nums: list[int], target: int) -> list[int]:
    pairs = itertools.combinations(range(len(nums)), 2)

    for first, second in pairs:
        if nums[first] + nums[second] == target:
            return [first, second]
