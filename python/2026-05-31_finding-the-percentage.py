# Problem : Finding The Percentage
# Topic   : hash-map
# Difficulty: easy
# Date    : 2026-05-31
# Source  : HackerRank

if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    target = student_marks[query_name]
    print(sum(target) / 3)
