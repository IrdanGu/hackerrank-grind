# Problem : Nested Lists
# Topic   : arrays
# Difficulty: easy
# Date    : 2026-05-31
# Source  : HackerRank

if __name__ == "__main__":
    student_score = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_score.append([name, score])

    unique_sorted = sorted(set(s[1] for s in student_score))
    second_lowest = unique_sorted[1]

    result = sorted([s[0] for s in student_score if s[1] == second_lowest])
    for name in result:
        print(name)
