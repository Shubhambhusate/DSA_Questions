def shipWithinDays(weights, days) -> int:

    high = sum(weights)  
    low = max(weights)

    while low <= high:

        mid = low + (high - low) // 2

        count_days = 1

        i = 0

        curr_sum = 0

        while i < len(weights):

            curr_sum += weights[i]

            if curr_sum > mid:

                count_days += 1

                curr_sum = weights[i]
            
            i += 1

        if count_days <= days:
            high = mid - 1
        else:
            low = mid + 1

    return low       

weights = weights = [1,4,4]
days = 3
print(shipWithinDays(weights,days))

