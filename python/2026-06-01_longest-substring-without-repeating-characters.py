# Problem   : Longest Substring Without Repeating Characters
# Topic     : sliding-window
# Difficulty: medium
# Date      : 2026-06-01
# Source    : HackerRank


def lengthOfLongestSubstring(s):
    char_index = {}
    longest = 0
    left = 0

    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        longest = max(longest, right - left + 1)

    return longest


print(lengthOfLongestSubstring("abcabcbb"))  # 3
print(lengthOfLongestSubstring("bbbbb"))  # 1
print(lengthOfLongestSubstring("pwwkew"))  # 3
print(lengthOfLongestSubstring(""))  # 0
