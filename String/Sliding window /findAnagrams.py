
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

def findAnagrams(s: str, p: str):

    arr_p = [0] * 26

    left,right = 0 , 0

    res = []

    for ch in p:

        index = ord(ch) - ord('a')
        arr_p[index] += 1

    arr_s_window = [0] * 26

    for i in range(len(s) - len(p) + 1):

        while right - left <= len(p) - 1:

            char = s[right]

            index = ord(char) - ord('a')

            arr_s_window[index] += 1

            right += 1

        if arr_p == arr_s_window:

            res.append(left)

        char = s[left]

        index = ord(char) - ord('a')

        arr_s_window[index] -= 1

        left += 1

    return res

s = "abab"
p = "ab"

print(findAnagrams(s,p))