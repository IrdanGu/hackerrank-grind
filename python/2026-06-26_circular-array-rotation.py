# Problem   : Circular Array Rotation
# Topic     : arrays
# Difficulty: easy
# Date      : 2026-06-26
# Source    : HackerRank

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#


def circularArrayRotation(a, k, queries):
    # Write your code here
    n = len(a)
    k_efektif = k % n
    result = []

    for q in queries:
        # Mencari indeks asli dari elemen yang diminta
        indeks_asli = (q - k_efektif) % n
        result.append(a[indeks_asli])

    return result


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
