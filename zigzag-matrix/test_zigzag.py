"""Run the zigzag solution against the cases.

    python3 zigzag-matrix/test_zigzag.py
"""

from zigzag import printZigZag

CASES = [
    ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 7, 6, 5, 9, 10, 11, 12]),
    ([[7, 2], [4, 9], [6, 1], [3, 8]], [7, 2, 9, 4, 6, 1, 8, 3]),
    # edge cases
    ([], []),                                  # empty matrix
    ([[5]], [5]),                              # single cell
    ([[1, 2, 3]], [1, 2, 3]),                  # single row: no reversal
    ([[1], [2], [3]], [1, 2, 3]),              # single column: reversing 1 item changes nothing
    ([[2, 4], [6, 8]], [2, 4, 8, 6]),          # all even values: row index decides, not the value
    ([[1, 2, 3], [4, 5], [6, 7, 8, 9]], [1, 2, 3, 5, 4, 6, 7, 8, 9]),  # rows of different length
]


if __name__ == "__main__":
    ok = 0
    for array, expected in CASES:
        got = printZigZag(array)
        mark = "OK  " if got == expected else "FAIL"
        ok += got == expected
        print(f"{mark} {array} -> {got} (expected {expected})")
    print(f"\n{ok}/{len(CASES)} passed")
