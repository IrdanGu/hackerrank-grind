# Problem : Between Two Sets
# Topic   : math
# Difficulty: medium
# Date    : 2026-06-02
# Source  : HackerRank

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def getTotalX(a, b):
    # Write your code here
    array_a = []
    for i in range(len(a)):
        for j in range(100):
            if j % a[i] == 0:
                array_a.append(j)
    print(array_a)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + "\n")

    fptr.close()
