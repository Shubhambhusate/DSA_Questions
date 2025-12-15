import re
def isPalindrome(s: str) -> bool:

    s = s.lower()

    left = 0 
    right = len(s) - 1

    while left <= right:

        char_left = s[left]

        char_right = s[right]

        if char_left.isalnum() and char_right.isalnum():

            if char_left != char_right:

                return False

            else:

                left += 1

                right -= 1
        else:

            if not char_left.isalnum():

                left += 1

            if not char_right.isalnum():

                right -= 1

    return True

print(isPalindrome("A man, a plan, a canal: Panama"))

