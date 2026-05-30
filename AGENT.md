# Agent Instructions — hackerrank-grind

You are an automation agent for a daily HackerRank grind repository.

## Your Job

When the user pastes a Python solution code, you will:

1. **Infer the problem name** from the code — look at function names, variable names, comments, or logic patterns. Convert to kebab-case slug (e.g. `two-sum`, `climbing-stairs`, `count-triplets`).

2. **Infer the topic** from the logic used:
   - Loops/arrays → `arrays`
   - dict/set → `hash-map`
   - sort() → `sorting`
   - recursion/memo → `dynamic-programming`
   - stack/queue → `stack-queue`
   - BFS/DFS/graph → `graphs`
   - math/modulo → `math`
   - string ops → `strings`
   - Default to `misc` if unclear.

3. **Infer the difficulty**:
   - Simple iteration or condition → `easy`
   - Multiple data structures or non-obvious logic → `medium`
   - Complex algorithm or optimization → `hard`
   - Default to `easy` if unsure.

4. **Get today's date** in `YYYY-MM-DD` format using the terminal.

5. **Create the solution file** at:
   ```
   python/YYYY-MM-DD_<problem-slug>.py
   ```
   The file content = the pasted code exactly, with this header prepended:
   ```python
   # Problem : <problem-name-title-case>
   # Topic   : <topic>
   # Difficulty: <difficulty>
   # Date    : YYYY-MM-DD
   # Source  : HackerRank
   
   ```

6. **Stage, commit, and push** using:
   ```bash
   git add python/YYYY-MM-DD_<problem-slug>.py
   git commit -m "solve: <problem-slug> | <topic> | <difficulty>"
   git push
   ```

---

## Rules

- Never modify existing files.
- Never create files outside the `python/` directory.
- If you cannot infer the problem name, ask the user: *"What is the problem name?"* — then proceed.
- Commit message must always follow: `solve: <slug> | <topic> | <difficulty>`
- Do not add extra files, do not touch README.md.

---

## Example

**User pastes:**
```python
def twoSum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in seen:
            return [seen[diff], i]
        seen[n] = i
```

**Agent does:**
- Problem: `two-sum`
- Topic: `hash-map`
- Difficulty: `easy`
- Date: `2026-05-31`
- Creates: `python/2026-05-31_two-sum.py`
- Commits: `solve: two-sum | hash-map | easy`
