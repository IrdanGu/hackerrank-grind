# Problem : Zigzag Sequence
# Topic   : sorting
# Difficulty: medium
# Date    : 2026-06-29
# Source  : HackerRank

"""
=== PROBLEM STATEMENT ===

Given an array of n distinct integers, rearrange it into the lexicographically
smallest zigzag sequence.

A zigzag sequence satisfies:
    arr[0] < arr[1] > arr[2] < arr[3] > arr[4] < ...

In other words, elements alternate between "valley" (local min) and "peak"
(local max) positions.

Input Format:
    - First line  : integer n (size of the array)
    - Second line : n space-separated distinct integers

Constraints:
    - 2  ≤ n       ≤ 10^5
    - 1  ≤ arr[i]  ≤ 10^9
    - All elements are distinct

Output Format:
    - n space-separated integers forming the lexicographically smallest zigzag.

------------------------------------------------------------------
Sample Input 0:
    7
    4 3 7 8 6 2 1

Sample Output 0:
    1 3 2 6 4 8 7

Explanation:
    Sort first       → [1, 2, 3, 4, 6, 7, 8]
    Swap at index 1  → [1, 3, 2, 4, 6, 7, 8]
    Swap at index 3  → [1, 3, 2, 6, 4, 7, 8]
    Swap at index 5  → [1, 3, 2, 6, 4, 8, 7]
    Verify           :  1<3>2<6>4<8>7 ✓
------------------------------------------------------------------
Sample Input 1:
    5
    1 2 3 4 5

Sample Output 1:
    1 3 2 5 4

Explanation:
    Sort first       → [1, 2, 3, 4, 5]
    Swap at index 1  → [1, 3, 2, 4, 5]
    Swap at index 3  → [1, 3, 2, 5, 4]
    Verify           :  1<3>2<5>4 ✓
------------------------------------------------------------------

=== END PROBLEM STATEMENT ===
"""

import os


def zigzagSequence(arr):
    # Step 1: sort to get elements in ascending order
    arr.sort()

    # Step 2: for every odd index i, swap arr[i] with arr[i+1]
    # This turns the sorted pair (valley, peak-candidate) into a peak,
    # while the previous element stays as the valley.
    for i in range(1, len(arr) - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


if __name__ == "__main__":
    fptr = open(os.environ.get("OUTPUT_PATH", "/dev/stdout"), "w")

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = zigzagSequence(arr)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
