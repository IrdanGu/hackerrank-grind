# Problem : Count Apples And Oranges
# Topic   : arrays
# Difficulty: easy
# Date    : 2026-06-02
# Source  : HackerRank

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#


def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    # angka = [1, 2, 3, 4, 5]
    hasil_apple = 0
    hasil_orange = 0
    angka_apple = [x + a for x in apples]
    angka_orange = [x + b for x in oranges]

    # Fixed: list.len() -> len(list)
    for i in range(len(angka_apple)):
        # Fixed: 'or' -> 'and' to check if it's strictly between s and t
        if angka_apple[i] >= s and angka_apple[i] <= t:
            hasil_apple += 1

    # Fixed: Iterate over the list 'angka_orange' instead of the integer 'hasil_orange'
    for i in range(len(angka_orange)):
        # Fixed: Checked the list element instead of the counter variable, and used 'and'
        if angka_orange[i] >= s and angka_orange[i] <= t:
            hasil_orange += 1

    print(hasil_apple)
    print(hasil_orange)


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
