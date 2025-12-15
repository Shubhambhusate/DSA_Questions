def searchInsert(nums : list[int], target: int) -> int:

    start = 0 

    end = len(nums) - 1

    while start <= end:

        mid = start + (end - start) // 2

        if nums[mid] == target:

            return mid 

        elif nums[mid] > target:

            end = mid - 1

        else:

            start = mid + 1

    return start 

nums = [1,3,5,6]
target = 7

print(searchInsert(nums,target))
