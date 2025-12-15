def findMin(nums):

    start = 0 

    end = len(nums) - 1

    minValue = float('inf')

    while start <= end:

        mid = start + (end-start)//2

        if nums[mid] >= nums[start]:

            minValue = min(minValue, nums[start])

            start = mid + 1

        elif nums[mid] <= nums[end]:

            minValue = min(minValue, nums[mid])

            end = mid - 1

    return minValue

nums = [3,1,2]

print(findMin(nums))
