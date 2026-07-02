# Problem : Jumping On Clouds Revisited
# Topic   : arrays
# Difficulty: easy
# Date    : 2026-07-02
# Source  : HackerRank

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e = 100
    n = len(c)
    i = 0

    while True:
        # Calculate the next cloud index circularly
        i = (i + k) % n

        # Deduct standard jump energy
        e -= 1

        # Deduct extra energy if it's a thunderhead
        if c[i] == 1:
            e -= 2

        # Stop the game if we reach the starting cloud
        if i == 0:
            break

    return e


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + "\n")

    fptr.close()
