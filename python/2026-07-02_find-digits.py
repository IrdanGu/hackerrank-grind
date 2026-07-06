# Problem : Find Digits
# Topic   : math
# Difficulty: easy
# Date    : 2026-07-02
# Source  : HackerRank

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#


def findDigits(n):
    # Write your code here
    string_num = str(n)
    count_me = 0
    for i in range(len(string_num)):
        if int(string_num[i]) != 0:
            if n % int(string_num[i]) == 0:
                count_me += 1
    return count_me


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + "\n")

    fptr.close()
