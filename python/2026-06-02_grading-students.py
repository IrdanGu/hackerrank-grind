# Problem : Grading Students
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
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades):
    rounded_grades = []

    for grade in grades:
        # If the grade is less than 38, it's failing and no rounding occurs.
        if grade < 38:
            rounded_grades.append(grade)
        else:
            # Find the remainder when divided by 5
            remainder = grade % 5

            # If remainder is 3 or 4, the next multiple of 5 is less than 3 away
            if remainder >= 3:
                rounded_grades.append(grade + (5 - remainder))
            else:
                rounded_grades.append(grade)

    return rounded_grades


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
