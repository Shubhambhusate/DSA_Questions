# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer.

# Example 1:

# Input: nums = [10,2]
# Output: "210"
# Example 2:

# Input: nums = [3,30,34,5,9]
# Output: "9534330"

nums = [3,30,34,5,9]
Output: "9534330"

def largestNumber(nums):

    for i in range (len(nums)):

        nums[i] = str(nums[i])

    for i in range(len(nums)):

        for j in range(i+1,len(nums)):

            if nums[i] + nums[j] < nums[j] + nums[i]:

                nums[i], nums[j] = nums[j],nums[i]

    return ''.join(nums)


print(largestNumber(nums))

