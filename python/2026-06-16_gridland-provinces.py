# Problem   : Gridland Provinces
# Topic     : dynamic-programming
# Difficulty: hard
# Date      : 2026-06-16
# Source    : HackerRank

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridlandProvinces' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#


def gridlandProvinces(s1, s2):
    N = len(s1)
    paths = set()

    def kumpulkan_rute(s_atas, s_bawah):
        # 1. Pre-compute Zig-zag Masters
        z0_list, z1_list = [], []
        for c in range(N):
            if c % 2 == 0:
                z0_list.append(s_atas[c] + s_bawah[c])  # Mulai dari atas
                z1_list.append(s_bawah[c] + s_atas[c])  # Mulai dari bawah
            else:
                z0_list.append(s_bawah[c] + s_atas[c])
                z1_list.append(s_atas[c] + s_bawah[c])
        z0 = "".join(z0_list)
        z1 = "".join(z1_list)

        # 2. Pre-compute potongan Kiri & Kanan (agar super cepat dan tidak TLE)
        left1 = [""] * (N + 1)
        left2 = [""] * (N + 1)
        right1 = [""] * (N + 1)
        right2 = [""] * (N + 1)

        for i in range(N):
            left1[i] = s_atas[: i + 1][::-1] + s_bawah[: i + 1]
            left2[i] = s_bawah[: i + 1][::-1] + s_atas[: i + 1]
        left1[-1] = ""
        left2[-1] = ""

        for j in range(N):
            right1[j] = s_atas[j:] + s_bawah[j:][::-1]
            right2[j] = s_bawah[j:] + s_atas[j:][::-1]
        right1[N] = ""
        right2[N] = ""

        # 3. Rakit rute dengan batas i dan j
        for i in range(-1, N):
            l1 = left1[i]
            l2 = left2[i]
            c = i + 1  # Titik mulai zig-zag

            for j in range(c, N + 1):
                r1 = right1[j]
                r2 = right2[j]

                # Rute skenario Ksatria yang datang dari baris Atas (l1)
                zig1 = z1[2 * c : 2 * j] if c % 2 == 0 else z0[2 * c : 2 * j]
                if (j - c) % 2 == 0:
                    paths.add(l1 + zig1 + r2)
                else:
                    paths.add(l1 + zig1 + r1)

                # Rute skenario Ksatria yang datang dari baris Bawah (l2)
                zig2 = z0[2 * c : 2 * j] if c % 2 == 0 else z1[2 * c : 2 * j]
                if (j - c) % 2 == 0:
                    paths.add(l2 + zig2 + r1)
                else:
                    paths.add(l2 + zig2 + r2)

    # Sapu jalan dari Kiri ke Kanan
    kumpulkan_rute(s1, s2)
    # Sapu jalan dari Kanan ke Kiri (Balikkan peta 180 derajat)
    kumpulkan_rute(s1[::-1], s2[::-1])

    # KEMBALIKAN JUMLAH-nya (Jangan di-print)
    return len(paths)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    p = int(input().strip())

    for p_itr in range(p):
        n = int(input().strip())

        s1 = input()
        s2 = input()

        result = gridlandProvinces(s1, s2)

        fptr.write(str(result) + "\n")

    fptr.close()
