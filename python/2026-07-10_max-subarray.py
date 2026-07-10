# Problem : Max Subarray
# Topic   : dynamic-programming
# Difficulty: medium
# Date    : 2026-07-10
# Source  : HackerRank

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
# Returns [max_subarray_sum, max_subsequence_sum] where:
#   - max_subarray_sum  : maximum sum of any contiguous subarray (Kadane's)
#   - max_subsequence_sum: maximum sum of any non-contiguous subsequence
#


def maxSubarray(arr):
    # --- Max contiguous subarray (Kadane's algorithm) ---
    max_sub = arr[0]
    current = arr[0]
    for i in range(1, len(arr)):
        current = max(arr[i], current + arr[i])
        max_sub = max(max_sub, current)

    # --- Max non-contiguous subsequence ---
    # Sum every positive element; if all are negative, pick the largest one
    positives = [x for x in arr if x > 0]
    max_seq = sum(positives) if positives else max(arr)

    return [max_sub, max_seq]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(" ".join(map(str, result)))
        fptr.write("\n")

    fptr.close()
