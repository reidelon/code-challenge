"""Valid Anagram — compare the sorted strings.

If two strings are anagrams, sorting their letters gives the same list.

Complexity: O(n log n) time (the sort), O(n) extra space for the sorted lists.
"""


def is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
