# You may recall that an array arr is a mountain array if and only if:

# arr.length >= 3
# There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

# Example 1:

# Input: arr = [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.


arr = [2,1,4,7,3,2,5]

def longestMountain(arr):

    lengthMountain = 1

    for i in range(1,len(arr)-1):

        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            left,right = i,i 

            while left > 0 and arr[left] > arr[left-1]:
                left -= 1
            
            while right < len(arr) - 1  and arr[right] > arr[right+1]:
                right += 1

            lengthMountain = max(lengthMountain, right - left + 1)

    return lengthMountain

print(longestMountain(arr))












