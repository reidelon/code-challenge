"""Run every Ransom Note solution against the same cases.

    python3 0383-ransom-note/test_ransom_note.py
"""

import counter

SOLUTIONS = [counter]

CASES = [
    ("a", "b", False),
    ("aa", "ab", False),
    ("aa", "aab", True),
    # edge cases
    ("a", "a", True),                  # same single letter
    ("abc", "cba", True),              # order does not matter
    ("abc", "ab", False),              # magazine shorter
    ("aab", "baa", True),
    ("aaa", "aab", False),             # letter exists, but not enough of it
    ("", "abc", True),                 # empty note can always be built
    ("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj", True),
    ("a" * 5000, "a" * 4999 + "b", False),  # long strings
]


if __name__ == "__main__":
    for solution in SOLUTIONS:
        print(f"== {solution.__name__}")
        passed = 0
        for note, magazine, expected in CASES:
            result = solution.can_construct(note, magazine)
            ok = result == expected
            passed += ok
            shown = (note, magazine) if len(magazine) <= 12 else f"[{len(note)} / {len(magazine)} chars]"
            print("OK  " if ok else "FAIL", shown, "->", result, "(expected", expected, ")")
        print(f"{passed}/{len(CASES)} passed\n")
