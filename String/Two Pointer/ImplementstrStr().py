# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

def strStr(haystack:str , needle: str) -> int:

    if len(needle) > len(haystack):

        return -1
    
    if len(needle) == 0:

        return 0
    
    for i in range(len(haystack) - len(needle) + 1):

        if haystack[ i : i + len(needle)] == needle:

            return i
        
    return -1

haystack = "sadbutsad"
needle = "sad"

print(strStr(haystack , needle))