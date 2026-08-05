# Problem : Sherlock And Squares
# Topic   : math
# Difficulty: easy
# Date    : 2026-08-05
# Source  : HackerRank

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#
# Optimized: O(1) per query using integer square root, instead of looping
# through every value in [a, b] and comparing floating-point sqrt results.
#
# The count of perfect squares in [a, b] equals:
#     floor(sqrt(b)) - floor(sqrt(a - 1))
#

def squares(a, b):
    return math.isqrt(b) - math.isqrt(a - 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
