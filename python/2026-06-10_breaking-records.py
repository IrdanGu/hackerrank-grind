# Problem   : Breaking Records
# Topic     : arrays
# Difficulty: easy
# Date      : 2026-06-10
# Source    : HackerRank

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#


def breakingRecords(scores):
    # Write your code here
    min_sem = scores[0]
    max_sem = scores[0]
    sum_min = 0
    sum_max = 0
    for i in range(1, len(scores), 1):
        if scores[i] > max_sem:
            sum_max += 1
            max_sem = scores[i]
        elif scores[i] < min_sem:
            sum_min += 1
            min_sem = scores[i]
    return [sum_max, sum_min]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
