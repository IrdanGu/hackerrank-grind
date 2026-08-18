# Problem : Non-Divisible Subset
# Topic   : math
# Difficulty: medium
# Date    : 2026-08-18
# Source  : HackerRank

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # 1. Siapkan dictionary dengan nilai awal 0 untuk semua kemungkinan sisa bagi (0 sampai k-1)
    all_number = {i: 0 for i in range(k)}
    
    # Hitung frekuensi setiap sisa bagi
    for num in s:
        all_number[num % k] += 1
        
    max_subset_size = 0
    
    # 2. Aturan sisa bagi 0: Tambahkan maksimal 1 jika ada
    if all_number[0] > 0:
        max_subset_size += 1
        
    # 3. Bandingkan sisa bagi x dengan k - x
    # Kita cukup melakukan perulangan sampai setengah dari k (k // 2) 
    # agar tidak menghitung pasangan yang sama dua kali.
    for i in range(1, (k // 2) + 1):
        if i == k - i:
            # 4. Khusus jika k genap dan i adalah titik tengah (k / 2)
            # Tambahkan maksimal 1 jika ada
            if all_number[i] > 0:
                max_subset_size += 1
        else:
            # Ambil kelompok sisa bagi yang anggotanya paling banyak
            max_subset_size += max(all_number[i], all_number[k - i])
            
    return max_subset_size

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
