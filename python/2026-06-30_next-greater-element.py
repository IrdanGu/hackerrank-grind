# Problem : Next Greater Element
# Topic   : stack-queue
# Difficulty: medium
# Date    : 2026-06-30
# Source  : HackerRank

"""
=== PROBLEM STATEMENT ===

Given an array of n integers, for each element find the FIRST element
to its right that is strictly greater than it.
If no such element exists, output -1 for that position.

Input Format:
    - First line  : integer n (size of the array)
    - Second line : n space-separated integers

Constraints:
    - 1  ≤ n       ≤ 10^5
    - -10^9 ≤ arr[i] ≤ 10^9

Output Format:
    - n space-separated integers representing the next greater element
      for each position (or -1 if none).

------------------------------------------------------------------
Sample Input 0:
    5
    4 5 2 10 8

Sample Output 0:
    5 10 10 -1 -1

Explanation:
    4  → next greater to the right is 5
    5  → next greater to the right is 10
    2  → next greater to the right is 10
    10 → no element to the right is greater → -1
    8  → no element to the right is greater → -1
------------------------------------------------------------------
Sample Input 1:
    6
    3 1 4 1 5 9

Sample Output 1:
    4 4 5 5 9 -1

Explanation:
    3  → next greater is 4
    1  → next greater is 4
    4  → next greater is 5
    1  → next greater is 5
    5  → next greater is 9
    9  → nothing to the right → -1
------------------------------------------------------------------

Algorithm (Monotonic Stack):
    Maintain a stack of indices whose "next greater" is still unknown.
    For each new element arr[i]:
      - While the stack is non-empty AND arr[i] > arr[stack top]:
            pop the index, record arr[i] as its next greater element.
      - Push i onto the stack.
    Any indices left in the stack at the end have no next greater → -1.

    Time  : O(n)  — each index is pushed and popped at most once.
    Space : O(n)  — stack in the worst case (descending array).

=== END PROBLEM STATEMENT ===
"""

import os


def nextGreaterElement(arr):
    n = len(arr)
    result = [-1] * n
    stack = []  # stores indices of elements awaiting their next greater

    for i in range(n):
        # Pop all indices whose next greater element is arr[i]
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)

    # Remaining indices in stack have no next greater element → stays -1
    return result


if __name__ == "__main__":
    fptr = open(os.environ.get("OUTPUT_PATH", "/dev/stdout"), "w")

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = nextGreaterElement(arr)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
