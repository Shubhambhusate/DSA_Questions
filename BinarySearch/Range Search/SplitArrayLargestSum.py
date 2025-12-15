def splitArray(nums: list[int], k: int) -> int:

    low = max(nums)
    high = sum(nums)
    minSum = sum(nums)

    while low <= high:

        mid = low + (high - low) // 2

        currSum = 0

        split_num = 1

        for values in nums:

            currSum += values

            if currSum > mid:

                split_num += 1

                currSum = values

        if split_num <= k:

            high = mid - 1

        else:

            low = mid + 1

    return low

print(splitArray(nums = [1,4,4], k = 3))