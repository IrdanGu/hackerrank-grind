# Problem : Mini Max Sum
# Topic   : arrays
# Difficulty: easy
# Date    : 2026-06-02
# Source  : HackerRank

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Write your code here
    min = 0
    max = 0
    arr = sorted(arr)
    for i in range(4, 0, -1):
        max += arr[i]
    for i in range(0, 4, +1):
        min += arr[i]
    print(min, max)


if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
