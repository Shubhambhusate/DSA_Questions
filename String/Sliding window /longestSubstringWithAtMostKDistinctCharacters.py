# Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

# Examples:
# Example 1:

# Input: s = 'eceba', k = 2
# Output: 3
# Explanation: The substring 'ece' contains 2 distinct characters.


def longestSubstringWithAtMostKDistinctCharacters(s: str, k: int) -> str:

    hash_map = {}

    maxLength = 0

    left = 0 

    for right in range(len(s)):

        char = s[right]

        hash_map[char] = hash_map.get(char,0) + 1

        while len(hash_map.keys()) > k:

            char_left = s[left]

            hash_map[char_left] = hash_map.get(char_left) - 1

            if hash_map[char_left] == 0:

                hash_map.pop(char_left)
            
            left += 1

        maxLength = max(right - left + 1, maxLength)

    return maxLength


s = 'eceba'
k = 2

print(longestSubstringWithAtMostKDistinctCharacters(s,k))