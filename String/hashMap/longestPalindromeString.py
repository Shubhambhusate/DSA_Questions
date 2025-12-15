
# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"

def calculatelongestPalindromeString(s,start,end):

    while start >=0 and end <= len(s) - 1 and s[start] == s[end]:

        start -=1 
        end += 1
        
    return start + 1, end - 1
    

def longestPalindrome(s):

    start , end = 0, 0 

    for i in range(len(s)-1):

        # for even 
        start1, end1 = calculatelongestPalindromeString(s,i,i+1) 

        # for odd
        start2, end2 = calculatelongestPalindromeString(s,i,i)

        if end - start < end1 - start1:
            start, end = start1, end1
        if end - start < end2 - start2:
            start, end = start2, end2

    return s[start:end+1]

s = "babad"

print(longestPalindrome(s))