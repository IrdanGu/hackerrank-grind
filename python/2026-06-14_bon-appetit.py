# Problem   : Bon Appetit
# Topic     : arrays
# Difficulty: easy
# Date      : 2026-06-14
# Source    : HackerRank

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#


def bonAppetit(bill, k, b):
    # Calculate the actual cost of shared items (total sum minus the item Anna didn't eat)
    actual_cost = (sum(bill) - bill[k]) // 2

    # Check if Brian charged her the correct amount
    if actual_cost == b:
        print("Bon Appetit")
    else:
        # Print the refund amount Brian owes Anna
        print(b - actual_cost)


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
