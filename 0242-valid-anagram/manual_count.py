"""Valid Anagram — without Counter.

Given two strings s and t, return True if t is an anagram of s,
and False otherwise.

An anagram uses exactly the same letters as the original, each one
the same number of times, just in a different order.

    s = "anagram", t = "nagaram"  ->  True
    s = "rat",     t = "car"      ->  False
    s = "aacc",    t = "ccac"     ->  False   (same letters, different counts)

Constraints: do NOT use collections.Counter, and do NOT sort.
Target: O(n) time.
"""
from collections import defaultdict


def is_anagram(s: str, t: str) -> bool:
    seen = set()
    if len(t) != len(s):
        return False

    for i in s:
        if i not in seen:
            seen.add(i)
            if s.count(i) != t.count(i):
                return False
    return True