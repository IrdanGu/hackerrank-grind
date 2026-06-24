# Problem   : Save the Prisoner!
# Topic     : math
# Difficulty: easy
# Date      : 2026-06-20
# Source    : HackerRank

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER s
#


def saveThePrisoner(n, m, s):
    # Hitung posisi terakhir jika kursi lurus (bukan melingkar)
    # lalu gunakan modulo n untuk menjadikannya melingkar
    last_position = (s + m - 1) % n

    # Karena kursi dimulai dari 1 (bukan 0), jika sisa baginya 0,
    # berarti permen jatuh tepat di kursi terakhir (n)
    if last_position == 0:
        return n
    else:
        return last_position
    return sweet


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + "\n")

    fptr.close()
