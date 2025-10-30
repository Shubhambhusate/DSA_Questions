# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

arr = [-1,0,1,2,-1,-4]

def threeSum(arr):

    arr.sort()

    result = []

    for i in range(len(arr)-2):
        if i > 0 and arr[i] == arr[i-1]:        
            # arr[i] == arr[i-1] skip the duplicate from the array 
            continue

        left, right = i + 1, len(arr) - 1

        while left < right:

            sum = arr[i] + arr[left] + arr[right]

            if sum == 0:

                result.append([arr[i],arr[left],arr[right]])

                while left < right and arr[left] == arr[left + 1]:
                    # arr[left] == arr[left - 1] skip the duplicate from the left array 

                    left = left + 1

                while left < right and arr[right] == arr[right -1]:
                    # arr[right] == arr[right - 1] skip the duplicate from the right array 

                    right = right - 1

                left = left + 1
                right = right -1

            elif sum > 0:

                right = right - 1

            else:

                left = left + 1

    return result 

print(threeSum([-1,0,1,2,-1,-4]))

                
 
