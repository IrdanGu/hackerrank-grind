# Problem   : Picking Numbers
# Topic     : hash-map
# Difficulty: easy
# Date      : 2026-06-18
# Source    : HackerRank
# Status    : INCOMPLETE — revisit later

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

    # 2. Iterasi untuk setiap angka yang unik
    for angka in frekuensi:
        print(angka)
        pass

    return maks_panjang


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + "\n")

    fptr.close()
