
# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.


def lengthOfLongestSubstring(s: str) -> int:

    hash = {}

    maxlength = 0

    left = 0

    for right in range(len(s)):

        char = s[right]

        if char in hash and hash[char] >= left:

            left = hash[char] + 1

        hash[char] = right

        maxlength = max(right - left + 1, maxlength)

    return maxlength

print(lengthOfLongestSubstring("abcabcbb"))