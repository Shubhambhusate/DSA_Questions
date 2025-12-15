import math

def reverse(x):

    sign = 1

    if x < 0:

        sign = -1

    x = abs(x)

    num = 0

    res = []

    while x >= 10:

        num = x % 10

        res.append(str(num))

        x = x // 10

    res.append(str(x))

    result = int(''.join(res)) * sign

    if result > (math.pow(2, 31) - 1) or result < (math.pow(-2, 31)):
        return 0
    
    return result

print(reverse(10))