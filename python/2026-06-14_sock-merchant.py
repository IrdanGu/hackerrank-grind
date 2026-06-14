# Problem   : Sock Merchant
# Topic     : sorting
# Difficulty: easy
# Date      : 2026-06-14
# Source    : HackerRank

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    sorted_numbers = sorted(ar)
    total = 0
    total_sebenarnya = 0

    for i in range(1, n):
        if sorted_numbers[i] == sorted_numbers[i - 1]:
            total += 1
        else:
            total_sebenarnya += (total + 1) // 2
            total = 0
    total_sebenarnya += (total + 1) // 2
    total = 0

    return total_sebenarnya

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
