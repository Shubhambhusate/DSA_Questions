def calculatelengthfromCentre(s,left,right):

    while left >= 0 and right < len(s) and s[left] == s[right]:

        left -= 1
        right += 1

    return right - left - 1
    
def lengthlongestPalindrome(s: str) -> int:

    max_len = 0

    for i in range(len(s)):

        max_len = max(max_len, calculatelengthfromCentre(s,i,i))

        max_len = max(max_len,calculatelengthfromCentre(s,i,i+1))

    return max_len

s = "baaaaaabaaaaad"

print(lengthlongestPalindrome(s))




