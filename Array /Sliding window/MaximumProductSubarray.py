# Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Note that the product of an array with a single element is the value of that element.

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.


nums = [-4,-3,-2]

def maxProduct(nums):

    maxProduct = nums[0]
    max_ending_here = nums[0]
    min_ending_here = nums[0]

    for i in range(1,len(nums)):

        list = [nums[i], nums[i] * max_ending_here, nums[i] * min_ending_here]

        max_ending_here = max(list)
        min_ending_here = min(list)

        maxProduct = max(maxProduct,max_ending_here)

    return maxProduct

print(maxProduct(nums))
