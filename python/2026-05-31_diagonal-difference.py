# Problem : Diagonal Difference
# Topic   : arrays
# Difficulty: easy
# Date    : 2026-05-31
# Source  : HackerRank

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    right = 0
    left = 0
    for i in range(len(arr)):
        right += arr[i][i]
    for i in range(len(arr)):
        j = len(arr) - i
        left += arr[i][n - 1 - i]
    print(right, left)
    return abs(right - left)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
