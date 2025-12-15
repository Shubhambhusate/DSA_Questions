# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"

# Output: 0

# Explanation:

# The character 'l' at index 0 is the first character that does not occur at any other index.


def firstUniqChar(s: str):

    arr = [0] * 26 

    for alpha in s:
        index = ord(alpha) - ord('a')
        arr[index] += 1

    for i in range(len(s)):
        alpha = s[i]
        index = ord(alpha) - ord('a')
        if arr[index] == 1:
            return i 

    return -1 

s = "leetcode"

print(firstUniqChar(s))


