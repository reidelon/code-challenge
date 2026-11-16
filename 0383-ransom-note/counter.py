"""Ransom Note — compare letter counts with Counter.

Given two strings ransomNote and magazine, return True if ransomNote can be
constructed by using the letters from magazine, and False otherwise.

Each letter in magazine can only be used once in ransomNote.

    ransom_note = "a",  magazine = "b"    ->  False
    ransom_note = "aa", magazine = "ab"   ->  False
    ransom_note = "aa", magazine = "aab"  ->  True

Constraints:
    1 <= len(ransom_note), len(magazine) <= 10^5
    both strings contain only lowercase English letters

Count the letters of both strings; every letter of the note must appear
at least as many times in the magazine. Counter returns 0 for a missing
letter, so one comparison covers "missing" and "not enough".

Complexity: O(n + m) time, O(1) extra space (at most 26 lowercase letters).
"""

from collections import Counter


def can_construct(ransom_note: str, magazine: str) -> bool:
    rn = Counter(ransom_note)
    ma = Counter(magazine)

    for letter in rn:
        if rn[letter] > ma[letter]:
            return False
    return True
