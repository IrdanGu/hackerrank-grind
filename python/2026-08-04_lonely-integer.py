# Problem : Lonely Integer
# Topic   : math
# Difficulty: easy
# Date    : 2026-08-04
# Source  : HackerRank

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
# All elements in 'a' appear exactly twice, except for one that appears once.
# XOR-ing every element cancels out all pairs (x ^ x = 0), leaving only the
# lonely integer.
#

def lonelyinteger(a):
    result = 0
    for num in a:
        result ^= num
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
