# Problem   : Minimum Swaps 2
# Topic     : arrays
# Difficulty: medium
# Date      : 2026-06-16
# Source    : HackerRank

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumSwaps' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def minimumSwaps(arr):
    n = len(arr)
    visited = [False] * n
    swaps = 0

    for i in range(n):
        # Skip if already in correct position or already visited
        if visited[i] or arr[i] == i + 1:
            continue

        # Trace the cycle starting at index i
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = arr[j] - 1  # follow the element to its correct index
            cycle_size += 1

        # A cycle of length k needs k-1 swaps to resolve
        swaps += cycle_size - 1

    return swaps


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + "\n")

    fptr.close()
