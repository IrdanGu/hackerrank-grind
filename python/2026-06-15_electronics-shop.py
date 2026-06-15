# Problem   : Electronics Shop
# Topic     : arrays
# Difficulty: easy
# Date      : 2026-06-15
# Source    : HackerRank

#!/bin/python3

import os
import sys


#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    arr_total = []
    for i in keyboards:
        for j in drives:
            arr_total.append(i + j)
    arr_total.sort()
    if arr_total[0] > b:
        return -1
    for i in range(len(arr_total)):
        if arr_total[i] > b:
            print(arr_total[i])
            return arr_total[i - 1]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + "\n")

    fptr.close()
