
# target = 11

# nums = [1,1,1,1,1,1,1,1]

# def minSubArrayLen(target, arr) -> int:

#     min_len = len(arr) + 1

#     flag = True

#     for i in range(len(arr)):

#         curr_sum = 0

#         for j in range(i,len(arr)):

#             curr_sum += arr[j]

#             if curr_sum >= target:

#                 min_len = min(min_len, j -i + 1)

#                 flag = False

#                 break

#     if flag:

#         return 0
    

# def minSubArrayLen(self, target: int, arr: List[int]) -> int:

#     min_len = len(arr) + 1

#     left = 0

#     curr_sum = 0

#     for right in range(len(arr)):

#         curr_sum += arr[right]

#         while curr_sum >= target:

#             min_len = min(min_len, right - left + 1)

#             curr_sum -= arr[left]

#             left += 1

#     if min_len != len(arr) + 1:

#         return min_len

#     else:

#         return 0

# print(minSubArrayLen(target, nums))

# nums = [2,2,2,2,2]

# def findLengthOfLCIS(arr):

#     max_len = 0

#     for i in range(1,len(arr)):

#         curr_len = 1

#         j = i

#         while j < len(arr) and arr[j] > arr[j-1]:

#             curr_len += 1

#             j += 1

#         max_len = max(max_len, curr_len)

#     return max_len

# print(findLengthOfLCIS(nums))


cardPoints = [96,90,41,82,39,74,64,50,30]

k = 8

def maxScore(cardPoints, k):

    total_points = 0

    maxScore = 0

    for i in range(len(cardPoints)):

        total_points += cardPoints[i]

    for i in range(k):

        sumCurrentWindow = 0

        for j in range(i,len(cardPoints) - k + i):

            sumCurrentWindow += cardPoints[j]

        maxScore = max(maxScore, total_points - sumCurrentWindow)

    return maxScore

print(maxScore(cardPoints,k))