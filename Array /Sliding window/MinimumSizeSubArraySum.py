# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

target = 7

nums = [2,3,1,2,4,3]

def minSubArrayLen(target,nums):

    min_len = len(nums) + 1
    curr_sum = 0
    left = 0

    for right in range(len(nums)):
        curr_sum += nums[right]

        while curr_sum >= target:
            min_len = min(min_len, right - left + 1)
            curr_sum -= nums[left]
            left += 1

    return min_len if min_len != len(nums) + 1 else 0

print(minSubArrayLen(target,nums))



