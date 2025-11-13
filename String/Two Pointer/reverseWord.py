def reverseWords( s: str) -> str:

    s = s.split(" ")

    left = 0
    right = len(s) - 1

    print(s)

    while left <= right:

        if len(s[left]) == 0:
            s.pop(left)
            right -= 1
        elif len(s[right])==0:
            s.pop(right)
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -=1

    return ' '.join(s)

s = " 3c      2zPeO dpIMVv2SG    1AM       o       VnUhxK a5YKNyuG     x9    EQ  ruJO       0Dtb8qG91w 1rT3zH F0m n G wU"

print(reverseWords(s))