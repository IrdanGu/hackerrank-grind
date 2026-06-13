# Problem   : Day Of Programmer
# Topic     : math
# Difficulty: easy
# Date      : 2026-06-13
# Source    : HackerRank

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#


def dayOfProgrammer(year):
    # Kasus khusus untuk tahun transisi 1918
    if year == 1918:
        return "26.09.1918"

    # Cek kondisi untuk sistem Kalender Julian (1700 - 1917)
    elif year < 1918:
        # Di kalender Julian, jika habis dibagi 4 berarti kabisat
        if year % 4 == 0:
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"

    # Cek kondisi untuk sistem Kalender Gregorian (1919 - 2700)
    else:
        # Aturan kabisat Gregorian: habis dibagi 400 ATAU (habis dibagi 4 dan tidak habis dibagi 100)
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + "\n")

    fptr.close()
