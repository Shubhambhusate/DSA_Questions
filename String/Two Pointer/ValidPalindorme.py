import re
def isPalindrome(s: str) -> bool:

    s = s.lower()
    pattern = r'[^a-z0-9]'

    # Replace all punctuation with empty string
    clean_s = re.sub(pattern, '', s)

    left = 0 

    right = len(clean_s) - 1 

    while left < right:

        if clean_s[left] == clean_s[right]:

            left += 1
            right -=1

        else:

            return False 

    return True

print(isPalindrome("A man, a plan, a canal: Panama"))

