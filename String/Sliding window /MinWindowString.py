# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

def minWindow(s: str, t: str) -> str:

    hash = {}

    for i in range(len(t)):
        char = t[i]
        hash[char] = hash.get(char,0) + 1

    left , right = 0 , 0

    count = 0 

    minLength = len(s)

    startIndex = 0

    while right < len(s) or right - left - 1 > len(t):

        while right < len(s):

            char = s[right]

            if char in hash:
                hash[char] = hash.get(char) - 1
                if hash[char] == 0:
                    count += 1
            else: 
                hash[char] = -1 

            right += 1

            if count == len(t):

                minLength = min(right - left + 1 , minLength)

                startIndex = left 

                break 


        while left < len(s):

            char = s[left]

            if char in hash:

                hash[char] = hash.get(char) + 1

                if hash[char] == 1:

                    count -= 1

            left += 1

            if count < len(t):

                minLength = min(right - left + 1 , minLength)

                startIndex = left - 1 

                break 

    return s[startIndex:startIndex+minLength]


s = "A"
t = "B"

print(minWindow(s,t))

