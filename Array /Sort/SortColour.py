# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]

nums = [2,0,2,1,1,0]

def sortColors(nums):

    p0,p1,p2 = 0,0,len(nums) - 1

    while p1 <= p2:

        if nums[p1] == 0:
            nums[p1],nums[p0] = nums[p0],nums[p1]
            p0 += 1
            p1 += 1

        elif nums[p1] == 2:
            nums[p1],nums[p2] = nums[p2],nums[p1]
            p2 -= 1

        else:

            p1 += 1

    return nums


print(sortColors(nums))