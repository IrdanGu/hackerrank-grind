# Problem   : Forming A Magic Square
# Topic     : arrays
# Difficulty: medium
# Date      : 2026-06-18
# Source    : HackerRank

#!/bin/python3

import math
import os
import random
import re
import sys


def formingMagicSquare(s):
    # All 8 valid 3x3 magic squares (rotations + reflections)
    pola_sempurna = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]

    semua_biaya = []

    for pola in pola_sempurna:
        biaya_saat_ini = 0

        for i in range(3):
            for j in range(3):
                biaya_saat_ini += abs(pola[i][j] - s[i][j])

        semua_biaya.append(biaya_saat_ini)

    return min(semua_biaya)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + "\n")

    fptr.close()
