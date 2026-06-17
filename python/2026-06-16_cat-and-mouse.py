# Problem   : Cat And Mouse
# Topic     : math
# Difficulty: easy
# Date      : 2026-06-16
# Source    : HackerRank

#!/bin/python3

import os
import sys


#
# Complete the catAndMouse function below.
#
def catAndMouse(x, y, z):
    #
    # Write your code here.
    #
    cat_a = abs(z - x)
    cat_b = abs(z - y)
    if cat_a == cat_b:
        return "Mouse C"
    elif cat_a < cat_b:
        return "Cat A"
    else:
        return "Cat B"


if __name__ == "__main__":
    f = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        f.write(result + "\n")

    f.close()
