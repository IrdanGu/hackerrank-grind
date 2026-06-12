# Problem   : Migratory Birds
# Topic     : arrays
# Difficulty: easy
# Date      : 2026-06-12
# Source    : HackerRank

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def migratoryBirds(arr):
    # Write your code here
    mapping_arr = [0, 0, 0, 0, 0]

    for i in range(len(arr)):
        mapping_arr[arr[i] - 1] += 1
        print(mapping_arr)
    for i in range(len(mapping_arr)):
        if mapping_arr[i] == max(mapping_arr):
            return i + 1


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
