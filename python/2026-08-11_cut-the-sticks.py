# Problem : Cut The Sticks
# Topic   : arrays
# Difficulty: easy
# Date    : 2026-08-11
# Source  : HackerRank

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Sort the array first
    arr.sort()
    
    # We always record the initial number of sticks
    result = [len(arr)]
    
    # Loop through the array starting from the second element (index 1)
    for i in range(1, len(arr)):
        # If the current stick is larger than the previous one,
        # it means all previous smaller sticks have been discarded.
        if arr[i] > arr[i-1]:
            # The number of remaining sticks is the total length minus the current index
            result.append(len(arr) - i)
            
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
