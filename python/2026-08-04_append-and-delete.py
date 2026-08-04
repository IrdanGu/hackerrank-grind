# Problem : Append And Delete
# Topic   : strings
# Difficulty: easy
# Date    : 2026-08-04
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
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Mencari panjang awalan huruf yang sama
    i = 0
    while i < len(s) and i < len(t) and s[i] == t[i]:
        i += 1
        
    # Menghitung minimal operasi (hapus sisa s + tambah sisa t)
    min_ops = (len(s) - i) + (len(t) - i)
    
    # Kondisi 1: Langkah minimal pas dengan k
    if min_ops == k:
        return "Yes"
    # Kondisi 2: Ada sisa langkah, dan sisa langkahnya genap (bisa hapus-tambah)
    elif min_ops < k and (k - min_ops) % 2 == 0:
        return "Yes"
    # Kondisi 3: Langkah sangat banyak, cukup untuk hapus total semua dan buat baru
    elif len(s) + len(t) <= k:
        return "Yes"
    # Jika tidak memenuhi syarat di atas, berarti gagal
    else:
        return "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
