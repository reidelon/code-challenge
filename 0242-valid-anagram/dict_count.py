"""Valid Anagram — count letters with a dict.

Given two strings s and t, return True if t is an anagram of s,
and False otherwise.

An anagram uses exactly the same letters as the original, each one
the same number of times, just in a different order.

    s = "anagram", t = "nagaram"  ->  True
    s = "rat",     t = "car"      ->  False
    s = "aacc",    t = "ccac"     ->  False   (same letters, different counts)

Constraints: use a plain dict (letter -> count). No Counter, no sort.

Add 1 for each letter of s, subtract 1 for each letter of t; if every
count ends at 0, both strings have the same letters the same number of times.
dict.get(letter, 0) avoids the KeyError the first time a letter appears.

Complexity: O(n) time (one pass over each string), O(k) extra space
(k = distinct characters), whatever characters the strings contain.
"""


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    counts = {}
    for letter in s:
        counts[letter] = counts.get(letter, 0) + 1
    for letter in t:
        counts[letter] = counts.get(letter, 0) - 1

    return all(count == 0 for count in counts.values())
