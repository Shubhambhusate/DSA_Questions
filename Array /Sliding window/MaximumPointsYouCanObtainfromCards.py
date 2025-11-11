# There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

# Your score is the sum of the points of the cards you have taken.

# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

# Example 1:

# Input: cardPoints = [1,2,3,4,5,6,1], k = 3
# Output: 12
# Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.

# Two pointer approach 

cardPoints = [1,2,3,4,5,6,1]

k = 3

def maxScore(cardPoints, k):

    left_sum = 0
    right_sum = 0
    max_sum = 0

    for i in range(k):
        left_sum += cardPoints[i]

    max_sum = left_sum

    for i in range(len(cardPoints)-1,len(cardPoints) - k -1, -1):
        right_sum += cardPoints[i]
        left_sum -= cardPoints[k-1]
        k -= 1
        max_sum = max(max_sum,left_sum+right_sum)

    return max_sum 

print(maxScore(cardPoints, k))

# Sliding window approach 

def maxScoreSlidingWindow(cardPoints, k):

    totalPoint = 0

    for i in range(len(cardPoints)):

        totalPoint += cardPoints[i]

    windowPoint = 0

    for i in range(len(cardPoints) - k):
        windowPoint += cardPoints[i]

    maxScore = totalPoint - windowPoint

    j = 0

    for i in range(len(cardPoints) - k, len(cardPoints)):

        windowPoint += cardPoints[i] - cardPoints[j]

        j += 1

        maxScore = max(maxScore,totalPoint - windowPoint)

    return maxScore

print(maxScoreSlidingWindow(cardPoints, k))

    




