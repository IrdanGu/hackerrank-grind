# Problem   : Climbing Leaderboard
# Topic     : arrays
# Difficulty: medium
# Date      : 2026-06-19
# Source    : HackerRank

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def climbingLeaderboard(ranked, player):
    # 1. Hapus duplikat skor di leaderboard untuk menerapkan Dense Ranking
    # Menggunakan dict.fromkeys() menjaga urutan asli tetap menurun
    ranked_unik = list(dict.fromkeys(ranked))

    hasil_peringkat = []

    # 2. Mulai pointer dari indeks terakhir (skor terendah di leaderboard)
    p = len(ranked_unik) - 1

    # 3. Iterasi setiap skor milik player
    for skor in player:
        # Pindahkan pointer naik selama skor player mampu mengalahkan leaderboard di posisi p
        while p >= 0 and skor >= ranked_unik[p]:
            p -= 1

        # 4. Tentukan peringkat player saat ini
        # Jika p < 0, berarti skor player mengalahkan peringkat 1, jadi peringkatnya otomatis 1
        if p < 0:
            hasil_peringkat.append(1)
        else:
            # Jika berhenti di indeks p, maka posisi player ada di bawah indeks p tersebut.
            # Rumus peringkatnya adalah: indeks p + 2
            hasil_peringkat.append(p + 2)

    return hasil_peringkat


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
