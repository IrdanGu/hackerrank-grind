# Problem   : Picking Numbers
# Topic     : hash-map
# Difficulty: easy
# Date      : 2026-06-18
# Source    : HackerRank

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def pickingNumbers(a):
    # Write your code here
    # 1. Hitung frekuensi setiap angka dalam array
    frekuensi = Counter(a)

    maks_panjang = 0
    print(frekuensi)
    # 2. Iterasi untuk setiap angka yang unik
    sementara = 0
    for angka in frekuensi:
        if sementara < frekuensi[angka] + frekuensi[angka + 1]:
            sementara = frekuensi[angka] + frekuensi[angka + 1]
        print(frekuensi[angka] + frekuensi[angka + 1])
        pass

    return sementara


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + "\n")

    fptr.close()
