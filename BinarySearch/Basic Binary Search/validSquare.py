def validSquare(num : int) -> bool:

    if num == 0 or num == 1:

        return True
    
    start = 0

    end = num

    while start <= end:

        mid = start + (end-start)//2

        if mid * mid == num:

            return True
        
        elif mid * mid > num:

            end = mid - 1

        else:

            start = mid + 1

        
    return False 

num = 16

print(validSquare(num))