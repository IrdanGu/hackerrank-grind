# Problem : Caesar Cipher
# Topic   : strings
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
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts the following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesarCipher(s, k):
    result = []
    for c in s:
        if c.isalpha():
            base = ord("a") if c.islower() else ord("A")
            result.append(chr((ord(c) - base + k) % 26 + base))
        else:
            result.append(c)
    return "".join(result)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + "\n")

    fptr.close()
