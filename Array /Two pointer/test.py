# arr = [2,7,11,15]
# target = 9


# def twoSum(arr, target):

#     hashMap = {}

#     for i,value in enumerate(arr):

#         compliment = target - value

#         if compliment in hashMap:

#             return [hashMap[compliment],i]
        
#         hashMap[value] = i

#     return [-1,-1]

# print(twoSum(arr, target))


# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# nums = [-1,0,1,2,-1,-4]

# def threeSum(nums):

#     nums.sort()

#     result = []

#     for i in range(1,len(nums)-2):

#         if i > 0 and nums[i] == nums[i-1]:

#             continue

#         left = i + 1

#         right = len(nums) - 1

#         while left < right:

#             sum = nums[i] + nums[left] + nums[right]

#             if sum == 0:

#                 result.append([nums[i] , nums[left] , nums[right]])

#                 while left < right and nums[left] == nums[left + 1]:

#                     left = left + 1

#                 while left < right and nums[right] == nums[right - 1]:

#                     right = right - 1

#                 left += 1
#                 right -= 1

#             elif sum < 0:

#                 left = left + 1

#             else:

#                 right = right - 1

#     return result

# print(threeSum(nums))

arr = [2,2,2]

def longestMountain(arr):

    start = None

    end = None

    for i in range(len(arr)-1):

        if i == 0 and arr[i] < arr[i + 1]:

            start = i 

        elif arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:

            if start is None: 

                start = i

            else:
                
                end = i

    if start is None and end is None:

        return 0

    return end - start


print(longestMountain(arr))

            


