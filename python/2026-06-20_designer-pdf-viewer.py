# Problem   : Designer PDF Viewer
# Topic     : arrays
# Difficulty: easy
# Date      : 2026-06-20
# Source    : HackerRank

#!/bin/python3

import math
import os
import random
import re
import string
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#


def designerPdfViewer(h, word):
    # Write your code here
    word = word.lower()
    simpan = []
    for huruf in word:
        n = string.ascii_lowercase.index(huruf)
        print(n)
        simpan.append(h[n])
    return max(simpan) * len(simpan)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + "\n")

    fptr.close()
