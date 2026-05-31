# Problem : Python Lists
# Topic   : arrays
# Difficulty: easy
# Date    : 2026-05-31
# Source  : HackerRank

if __name__ == "__main__":
    N = int(input())
    container = []

    for i in range(N):
        command_line = input().split()
        cmd = command_line[0]

        if cmd == "insert":
            # Convert both index and value to integers
            container.insert(int(command_line[1]), int(command_line[2]))
        elif cmd == "print":
            print(container)
        elif cmd == "remove":
            # Convert value to integer
            container.remove(int(command_line[1]))
        elif cmd == "append":
            # Convert value to integer
            container.append(int(command_line[1]))
        elif cmd == "sort":
            container.sort()
        elif cmd == "pop":
            container.pop()
        elif cmd == "reverse":
            container.reverse()
