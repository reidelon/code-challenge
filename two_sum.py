"""Two Sum (LeetCode 1).

Given a list of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to `target`. There is exactly one valid
answer, and the same element can't be used twice. Any order is accepted.

Approach (one pass with a dict): walk the list once. For each value, compute
the number still needed (`target - value`) and check whether it was already
seen. If so, return both indices; if not, store the value with its index.
Checking before storing keeps an element from pairing with itself.

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


if __name__ == "__main__":
    cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        # edge cases
        ([0, 4, 3, 0], 0, [0, 3]),        # duplicate zeros, far apart
        ([1, 5, 5], 10, [1, 2]),          # duplicates at the end
        ([5, 1, 5], 10, [0, 2]),          # duplicates apart
        ([-3, 4, 3, 90], 0, [0, 2]),      # negative + positive
        ([1, 2, 3, 4, 5], 9, [3, 4]),     # pair at the end
        ([15, 11, 7, 2], 9, [2, 3]),      # unsorted
        ([1000000000, 2, 1000000000], 2000000000, [0, 2]),  # large numbers
    ]
    for nums, target, expected in cases:
        result = two_sum(nums, target)
        ok = result is not None and sorted(result) == sorted(expected)
        print("OK  " if ok else "FAIL", nums, target, "->", result, "(expected", expected, ")")
