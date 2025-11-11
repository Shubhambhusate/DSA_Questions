

arr = [2,7,11,15]
target = 9

# Brute force approach space is constant and time complexity Order of N square

def twoSum(arr,target):

    for i in range(len(arr)):

        for j in range(i+1,len(arr)):

            if (arr[i]+arr[j]) == target:

                return [i,j]
            
    return [-1,-1]

# The enumerate() function in Python is a built-in function that adds a counter to an iterable (like a list, tuple, or string) and returns it as an enumerate object.

def twoSumOptimise(arr,target):

    nums_map = {}

    for i, value in enumerate(arr):

        compliment = target - value

        if compliment in nums_map:

            return [nums_map[compliment],i]
        
        nums_map[value] = i

    return [-1,-1]

print(twoSum(arr,target))

print(twoSumOptimise(arr,target))
