# Problem : Permutation Equation
# Topic   : arrays
# Difficulty: medium
# Date    : 2026-06-27
# Source  : HackerRank

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#


def permutationEquation(p):
    # Write your code here
    result = []
    for i in range(len(p)):
        z = p.index(i + 1) + 1
        y = p.index(z) + 1
        result.append(y)
    return result


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
