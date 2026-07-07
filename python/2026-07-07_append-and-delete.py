# Problem : Append And Delete
# Topic   : strings
# Difficulty: easy
# Date    : 2026-07-07
# Source  : HackerRank

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts the following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#


def appendAndDelete(s, t, k):
    common_length = 0

    # 1. Find the length of the identical prefix
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            common_length += 1
        else:
            break

    # 2. Calculate the absolute minimum operations required
    # (Delete differing characters from 's', then append missing characters for 't')
    min_ops = (len(s) - common_length) + (len(t) - common_length)

    # 3. Evaluate if exactly 'k' operations can be achieved
    if min_ops <= k and (k - min_ops) % 2 == 0:
        # We can waste pairs of operations by deleting and appending the same character
        return "Yes"
    elif len(s) + len(t) <= k:
        # We have enough operations to completely delete 's' (including empty deletions) and build 't'
        return "Yes"
    else:
        # Not enough operations, or the leftover operations are an odd number we can't burn
        return "No"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + "\n")

    fptr.close()
