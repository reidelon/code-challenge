"""Valid Anagram — compare letter counts with Counter.

Two strings are anagrams when every letter appears the same number of
times in both, so build a Counter for each and compare them.

Complexity: O(n + m) time, O(k) extra space (k = distinct letters).
"""

from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
