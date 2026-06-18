# Problem   : Count Triplets
# Topic     : hash-map
# Difficulty: medium
# Date      : 2026-06-18
# Source    : HackerRank

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'countTriplets' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY arr
#  2. LONG_INTEGER r
#


def countTriplets(arr, r):
    # left  : frequency of elements already processed (potential first/second of triplet)
    # right : frequency of elements not yet processed (potential second/third of triplet)
    left = defaultdict(int)
    right = defaultdict(int)

    for val in arr:
        right[val] += 1

    count = 0
    for val in arr:
        # Remove current element from "right" window before counting
        right[val] -= 1

        # Treat val as the middle element b of triplet (a, b, c)
        # where a = b/r (must divide evenly) and c = b*r
        if val % r == 0:
            count += left[val // r] * right[val * r]

        # Slide current element into the "left" window
        left[val] += 1

    return count


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    r = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + "\n")

    fptr.close()
