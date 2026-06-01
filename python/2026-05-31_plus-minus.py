# Problem : Plus Minus
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
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    n = len(arr)
    positive = 0
    negative = 0
    zeros = 0
    for i in range(n):
        if arr[i] == 0:
            zeros += 1
        elif arr[i] > 0:
            positive += 1
        elif arr[i] < 0:
            negative += 1
    print(positive / n)
    print(negative / n)
    print(zeros / n)


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
