# Problem : Extra Long Factorials
# Topic   : math
# Difficulty: medium
# Date    : 2026-07-02
# Source  : HackerRank

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#


def extraLongFactorials(n):
    # Write your code here
    hasil = 1
    for i in range(n, 0, -1):
        hasil *= i
    print(hasil)


if __name__ == "__main__":
    n = int(input().strip())

    extraLongFactorials(n)
