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

# arr = [2,2,2]

# def longestMountain(arr):

#     start = None

#     end = None

#     for i in range(len(arr)-1):

#         if i == 0 and arr[i] < arr[i + 1]:

#             start = i 

#         elif arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:

#             if start is None: 

#                 start = i

#             else:
                
#                 end = i

#     if start is None and end is None:

#         return 0

#     return end - start


# print(longestMountain(arr))


# def three_sum(nums):

#     nums.sort()

#     res = []

#     for i in range(len(nums) - 2):
#         # to skip the duplicate element
#         if i != 0 and nums[i] == nums[i-1]:
#             continue

#         left = i + 1
#         right = len(nums) - 1

#         while left < right:

#             sum = nums[i] + nums[left] + nums[right]

#             if sum == 0:

#                 res.append([nums[i], nums[left] ,nums[right]])

#                 while left < right and nums[i] == nums[i+1]:

#                     left += 1

#                 while left < right and nums[i] == nums[i-1]:

#                     right -= 1

#             elif sum > 0:

#                 right -= 1

#             else:

#                 left += 1

#     return res


# print(three_sum([-1,0,1,2,-1,-4]))


# def three_closest_sum(nums, target):

#     nums.sort()

#     closest_sum = nums[0] + nums[1] + nums[2]

#     for i in range(len(nums) - 2):

#         left = i + 1
#         right = len(nums) - 1

#         current_sum = nums[i] + nums[left] + nums[right]

#         if abs(current_sum - target) < abs(closest_sum - target):

#             closest_sum = current_sum

#         if current_sum == target:

#             left += 1
#             right -= 1

#         elif current_sum > target:

#             right -= 1

#         else:

#             left += 1

#     return closest_sum

# print(three_closest_sum([-1,2,1,-4], 1))

# def removeDuplicatesFromSortedArray(nums):

#     if len(nums) < 2:
#         return len(nums)
    
#     i = 1
    
#     while i < len(arr):

#         if arr[i] == arr[i - 1]:

#             arr.pop(i)

#         else:

#             i+=1

#     return len(nums)

# arr = [0,0,1,1,1,2,2,3,3,4]
# print(removeDuplicatesFromSortedArray(arr))


# def merge(nums):

#     nums.sort()

#     res = []

#     res.append(nums[0])

#     for i in range(1, len(nums)):

#         if res[-1][0] <= nums[i][1] and res[-1][1] >= interval[i][1]:

#             continue

#         elif res[-1][1] >= nums[i][0]:

#             res[-1][1] = nums[i][1]

#         else:

#             res.append(nums[i])

#     return res

# interval = [[1,3],[2,6],[8,10],[15,18]]

# print(merge(interval))


# def insert(interval, newInterval):
        
#         i = 0 

#         res = []

#         while i < len(interval) and interval[i][1] < newInterval[0]:

#             res.append(interval[i])

#             i += 1

#         while i < len(interval) and interval[i][0] <= newInterval[1]:

#             newInterval[0] = min(interval[i][0], newInterval[0])
#             newInterval[1] = max(interval[i][1], newInterval[1])

#             i += 1

#         res.append(newInterval)

#         while i < len(interval):

#             res.append(interval[i])

#             i += 1

#         return res


# intervals =  [[1,3],[6,9]]
# newInterval = [2,5]

# print(insert(intervals, newInterval))

# def maximumMeetings(start,end):

#     data_list = []
    
#     for i in range(len(start)):
        
#         data_list.append([start[i], end[i], i])
        
#         data_list.sort(key = lambda x : x[1])
        
#     free_time = data_list[0][1]
    
#     count = 1
    
#     position = []
    
#     position.append(data_list[0][2])
    
#     for i in range(1, len(start)):
        
#         if data_list[i][0] > free_time:
            
#             count += 1

#             free_time = data_list[i][1]
            
#             position.append(data_list[i][2])

#     return count, position

# start = [1, 3, 0, 5, 8, 5] 
# end =  [2, 4, 6, 7, 9, 9]

# print(maximumMeetings(start,end))


# def meetingRoomsII(nums):

#     nums.sort(key = lambda x:x[1])

#     count = 1

#     free_time = nums[0][1]

#     for i in range(1,len(nums)):

#         if nums[i][0] < free_time:

#             count +=1 

#             free_time = nums[i][1]

#     return count

# nums = [[0, 30],[5, 10],[15, 20]]

# print(meetingRoomsII(nums))

# Input: [1, 5, 1, 1, 6, 4, 3]
# Output: [1, 6, 1, 5, 1, 4]

# [1,1,1,3,4,5,6]

# [1,4,1,5,1,6,3]

# [1,1,1,4,5,6]

# [1,]


# def wigglesort(nums):

#     sorted_arr = sorted(nums)

#     start = 0

#     mid = (len(nums) + 1) // 2 

#     i = 0

#     while i < len(nums):

#         if i % 2 == 0:

#             nums[i] = sorted_arr[start]

#             start += 1

#         else:

#             nums[i] = sorted_arr[mid]

#             mid += 1

#         i += 1

#     print(nums)


# nums = [1, 5, 1, 1, 6, 4]

# wigglesort(nums)


# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]


# def mergeSortArray(nums1,nums2,m,n):

#     k = m + n - 1

#     m = m - 1

#     n = n - 1

#     while m >= 0 and n >= 0:

#         if nums1[m] < nums2[n]:

#             nums1[k] = nums2[n]

#             k -= 1
#             n -= 1
        
#         else:

#             nums1[k] = nums1[m]

#             k -= 1
#             m -= 1

#     while n >= 0:

#         nums1[k] = nums2[n]

#         k -= 1
#         n -= 1


# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3

# print(mergeSortArray(nums1,nums2,m,n))

# target = 15
# nums = [5,1,3,5,10,7,4,9,2,8]

# def minimumSizeSubarraySum(nums, target):

#     total_sum = sum(nums)

#     if total_sum < target:

#         return 0

#     min_length = len(nums) + 1

#     for i in range(len(nums)):

#         current_sum = 0

#         for j in range(i,len(nums)):

#             current_sum += nums[j]

#             if current_sum >= target:

#                 min_length = min(min_length , (j - i + 1))

#     if min_length == len(nums) + 1:
#         return 0
#     else:
#         return min_length

# print(minimumSizeSubarraySum(nums, target))


# target = 15
# nums = [5,1,3,5,10,7,4,9,2,8]

# def minimumSizeSubarraySumOptimise(nums, target):

#     total_sum = sum(nums)

#     if total_sum < target:

#         return 0

#     min_length = len(nums) + 1

#     current_sum = 0

#     left = 0

#     for right in range(len(nums)):

#         current_sum = current_sum + nums[right]

#         while current_sum >= target:

#             min_length = min (min_length, right - left + 1)

#             current_sum -= nums[left]

#             left += 1

#     if min_length == len(nums) + 1:
#         return 0
#     else:
#         return min_length

# print(minimumSizeSubarraySumOptimise(nums, target))

# nums = [0,1,2,3,4,5,4,3,2,1,0]


# def longestMountainInArray(nums):

#     max_length = 0

#     for i in range(1,len(nums)-1):

#         if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
            
#             start = i 
#             end = i

#             while start > 0 and nums[start] > nums[start - 1]:

#                 start -= 1

#             while end < len(nums) - 1 and nums[end] > nums[end + 1]:

#                 end += 1

#             max_length = max(max_length, end - start + 1)

#     return max_length

# print(longestMountainInArray(nums))


# cardPoints = [11,49,100,20,86,29,72]
# k = 4

# def maxScore(cardPoints,k):

#     total_sum = sum(cardPoints)

#     curr_sum = sum(cardPoints[:len(cardPoints) - k])

#     max_sum = total_sum - curr_sum

#     left = 0

#     right = len(cardPoints) - k

#     while k > 0:

#         curr_sum = curr_sum + cardPoints[right] - cardPoints[left]

#         left += 1

#         right += 1

#         max_sum = max (max_sum ,total_sum - curr_sum)

#         k -= 1

#     return max_sum

# print(maxScore(cardPoints,k))


# def maxProduct(nums):

#     max_product = nums[0]
#     min_product_here = nums[0]
#     max_product_here = nums[0]

#     for i in range(1, len(nums)):

#         list = [nums[i], min_product_here * nums[i], max_product_here * nums[i]]

#         min_product_here = min(list)
#         max_product_here = max(list)

#         max_product = max(max_product, max_product_here)

#     return max_product 

# nums = [2,3,-2,4]

# print(maxProduct(nums))


# 442. Find All Duplicates in an Array

# def findDuplicates(nums):

#     pointer = 0 
#     index = 1

#     result = []

#     while pointer < len(nums):

#         while nums[pointer] != index:

#             res = nums[pointer] - 1

#             if nums[res] == nums[pointer]:

#                 if nums[pointer] not in result:
                
#                     result.append(nums[pointer])

#                 break

#             else:

#                 nums[pointer], nums[res] = nums[res], nums[pointer]

#         pointer += 1
#         index += 1

#     return result


# nums = [1]

# print(findDuplicates(nums))



# def findDuplicatesOptimise(nums):

#     result = []

#     for i in range(len(nums)):

#         index = abs(nums[i]) - 1

#         if nums[index] < 0:

#             result.append(abs(nums[index])

#         else:

#             nums[index] = -nums[index]

    
#     return result


# nums = [4,3,2,7,8,2,3,1]

# print(findDuplicatesOptimise(nums))


# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"

# def reverseWords(s):

#     res = s.split(" ")

#     left = 0 

#     right = len(res) - 1

#     while left <= right:

#         if len(res[left]) == 0:

#             res.pop(left)

#             right -= 1

#         elif len(res[right]) == 0:

#             res.pop(right)

#             right -= 1

#         else:

#             res[left] ,  res[right]  = res[right] , res[left]

#             left += 1
#             right -= 1

#     return ' '.join(res)

# s = "the  sky    is   blue"
# print(reverseWords(s))



def gettingPalindromeString(s, start, end):

    while start >= 0 and end <= len(s) - 1 and s[start] == s[end]:

        start -= 1
        end += 1

    return start + 1, end - 1

# def longestPalindromicSubstring(s: str) -> str:

#     start = 0 
#     end = 0

#     for i in range(len(s)):

#         # To handle odd string length

#         start1, end1 = gettingPalindromeString(s, i, i)

#         # To handle even string length 

#         start2, end2 = gettingPalindromeString(s,i,i+1)

#         if end1 - start1 > end - start:

#             end, start = end1 , start1

#         if end2 - start2 > end - start:

#             end, start = end2, start2

#     return s[start: end+1]

# print(longestPalindromicSubstring("babad"))


# def lengthOfLongestSubstring(s: str):
#     hash = {}

#     maxlength = 0

#     left = 0

#     for right in range(len(s)):

#         char = s[right]

#         if char in hash and hash[char] >= left:

#             left = hash[char] + 1

#         hash[char] = right

#         maxlength = max(right - left + 1, maxlength)

#     return maxlength

# print(lengthOfLongestSubstring("abba"))     


# def longestSubstringWithAtMostKDistinctCharacters(s:str,k:int) -> int:

#     max_len = 0

#     left = 0

#     hash_map = {}

#     for right in range(len(s)):

#         char = s[right]

#         hash_map[char] = hash_map.get(char, 0) + 1

#         while len(hash_map.keys()) > k:

#             char_left = s[left]
#             hash_map[char_left] -= 1
#             if hash_map[char_left] == 0:
#                 hash_map.pop(char_left)
            
#             left += 1

#         max_len = max(max_len, right - left + 1)

#     return max_len

# s = 'eceba'
# k = 2

# print(longestSubstringWithAtMostKDistinctCharacters(s,k))


# def longestRepeatingCharacterReplacement(s: str, k : int) -> int:

#     max_len = 0
#     hashmap = {}
#     left = 0
#     for right in range(len(s)):

#         char_right = s[right]

#         hashmap[char_right] = hashmap.get(char_right, 0) + 1

#         max_frequency = max(hashmap.values())

#         while right - left + 1 - max_frequency > k:

#             char_left = s[left]

#             hashmap[char_left] -= 1

#             left += 1

#             max_frequency = max(hashmap.values())

#         max_len = max(max_len, right - left + 1)

#     return max_len


# s = 'AABABBA'
# k = 1

# print(longestRepeatingCharacterReplacement(s, k ))

# def findAnagrams(s: str, p: str) -> list:

#     arr_p = [0] * 26

#     res = []

#     for i in range(len(p)):

#         char = p[i]

#         index = ord(char) - ord('a')

#         arr_p[index] += 1 

#     right, left = 0, 0

#     arr_window = [0] * 26

#     for i in range(len(s) - len(p) + 1):

#         while right - left < len(p):

#             char = s[right]

#             index = ord(char) - ord('a')

#             arr_window[index] += 1

#             right += 1

#         if arr_p == arr_window:

#             res.append(i)
        
#         char_left = s[left]

#         index = ord(char_left) - ord('a')

#         arr_window[index] -= 1

#         left += 1

#     return res

# s = "cbaebabacd"
# p = "abc"

# print(findAnagrams(s,p))

# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.

# Note: The characters in the array beyond the returned length do not matter and should be ignored.

 

# Example 1:

# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

# def compress (chars) -> int:

#     hash_map = {}

#     for i in range(len(chars)):

#         char = chars[i]

#         hash_map[char] = hash_map.get(char, 0) + 1

#     res = []

#     for key, values in hash_map.items():

#         res.append(key)

#         if values == 1:

#             pass

#         else:

#             while values >= 10:

#                 res.append(str(values//10))

#                 values = values % 10

#             res.append(str(values))

#     return res

# print(compress(chars))


# def compress(chars) -> int:

#     left = 0

#     grouplength = 1

#     for right in range(1, len(chars)):

#         if chars[right] == chars[right - 1]:

#             grouplength += 1

#         else:
                
#             chars[left] = chars[right - 1]
#             left += 1

#             if grouplength > 1:
#                 for c in str(grouplength):
#                     chars[left] = c
#                     left += 1

#             grouplength = 1

#     chars[left] = chars[-1]
#     left += 1
#     if grouplength > 1:
#         for c in str(grouplength):
#             chars[left] = c
#             left += 1
        
#     return chars[:left]

# chars = ["a","c","c","c","b","b","b","b","b","b","b","b","b","b","b","b"]
# print(compress(chars))


# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# strs = ["eat","tea","tan","ate","nat","bat"]

# def groupAnagrams(strs: list[str]):

#     hash_map = {}

#     for i in range(len(strs)):

#         element = ''.join(sorted(strs[i]))

#         if element in hash_map:

#             hash_map[element].append(strs[i])

#         else:

#             hash_map[element] = [strs[i]]

#     return list(hash_map.values())

    # result = []

    # for values in hash_map.values():

    #     res = []

    #     for value in values:

    #         res.append(strs[value])

    #     result.append(res)

    # return hash_map

# strs = ["eat","tea","tan","ate","nat","bat"]

# print(groupAnagrams(strs))

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:

# Input: x = 123
# Output: 321

# import math

# x = 0

# def reverse(x):


#     if x == 0:

#         return 0

#     sign = 1

#     if x < 0:

#         sign = -1

#     res = ""

#     x = abs(x)

#     while x > 0:

#         rem = x % 10 

#         rem = str(rem)

#         res += rem

#         x = x//10

#     res = int(res)

#     res = res * sign

#     if res > (-math.pow(2, 31)) and res < (math.pow(2, 31) - 1):

#         return res
    
#     else:

#         return 0


# print(reverse(x))


# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

# The algorithm for myAtoi(string s) is as follows:

# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
# Return the integer as the final result.

 

# Example 1:

# Input: s = "42"

# Output: 42

# Explanation:

# The underlined characters are what is read in and the caret is the current reader position.
# Step 1: "42" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "42" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "42" ("42" is read in)
#            ^
# Example 2:

# Input: s = " -042"

# Output: -42

# Explanation:

# Step 1: "   -042" (leading whitespace is read and ignored)
#             ^
# Step 2: "   -042" ('-' is read, so the result should be negative)
#              ^
# Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
#                ^
# Example 3:

# Input: s = "1337c0d3"

# Output: 1337

# Explanation:

# Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
#              ^
# Example 4:

# Input: s = "0-1"

# Output: 0

# Explanation:

# Step 1: "0-1" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
#           ^
# Example 5:

# Input: s = "words and 987"

# Output: 0

# Explanation:

# Reading stops at the first non-digit character 'w'.

# import math

# def  myAtoi(s):

#     flag = True
#     sign = 1
#     result_arr = ["0"]

#     for i in range(len(s)):

#         if (s[i] == '+' and s[i+1] == '-') or (s[i] == '+' and s[i+1] == '-'):

#             return 0

#         if flag:

#             if s[i] == " ":
#                 continue

#             if s[i] == "+":
#                 flag = False
#                 continue

#             if s[i] == "-":
#                 flag = False
#                 sign = -1
#                 continue

#             if s[i] < '0' or s[i] > '9':
#                 break

#             flag = False

#             result_arr.append(s[i])

#         else:

#             if s[i] < '0' or s[i] > '9':
#                 break

#             result_arr.append(s[i])

#     result_arr = int(''.join(result_arr)) * sign

#     if result_arr > (-math.pow(2, 31)) and result_arr < (math.pow(2, 31) - 1):

#         return result_arr

#     else:

#         return 0


# s = "   -042"

# print(myAtoi(s))


# A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. 
# For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses while "192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses.

# queryIP = "192.168@1.1"

# def validIPv4Address(queryIP: str) -> str:

#     flag = True

#     queryIP = queryIP.split(".")

#     if len(queryIP) != 4:

#         flag = False
    
#     if flag:

#         for i in range(len(queryIP)):

#             char = queryIP[i]

#             if len(char) >= 1 and len(char) <= 3:

#                 pass

#             else:

#                 flag = False

#                 break

#             if (flag and char > '255' or char < '0'):

#                 flag = False
            
#             for c in char:

#                 if (flag and len(char) > 1 and char[0] == '0'):

#                     flag = False

#     return "IPv4" if flag else False


# print(validIPv4Address("172.16.254.10"))


# def validIPv6Address(queryIP: str) -> str:

#     flag = True

#     queryIP = queryIP.split(":")

#     if len(queryIP) != 8:

#         flag = False
    
#     if flag:

#         for i in range(len(queryIP)):

#             char = queryIP[i]

#             if len(char) >= 1 and len(char) <= 4:

#                 pass

#             else:

#                 flag = False

#                 break
            
#             for c in char:

#                 if (c >= '0' and c <= '9' ) or (c >= 'a' and c <= 'f') or  (c >= 'A' and c <= 'F'):

#                     flag = True

#                 else:

#                     flag = False

#                     break  

#             if flag == False:

#                 break 

#     return "IPv6" if flag else False

# print(validIPv6Address("f:f:f:f:f:f:f:f"))




# def validIPAddress(queryIP: str) -> str:

#     if len(queryIP) <= 15:

#         validIPv4AddressVar = validIPv4Address(queryIP)

#         if validIPv4AddressVar == "IPv4":

#             return "IPv4"

#     else:

#         validIPv6AddressVar = validIPv6Address(queryIP)

#         if validIPv6AddressVar == "IPv6":

#             return "IPv6"

#     return "Neither"
    
# queryIP = "256.256.256.256"

# print(validIPAddress(queryIP))


# s = "100[leetcode]"

# def decodeString(s):

#     res = ""

#     num_stack = []

#     string_stack = []

#     num = ''

#     for i in range(len(s)):

#         char = s[i]

#         if char.isdigit():
#             num += char 
#             if i + 1 == len(s) or not s[i + 1].isdigit():
#                 num_stack.append(int(num))
#                 num = ""

#         elif char.isalpha() or char == '[':

#             string_stack.append(char)

#         elif char == ']':

#             res = ''

#             while string_stack[-1] != '[':

#                 temp = string_stack.pop()

#                 res = temp + res

#             number = num_stack.pop()

#             res = res * number

#             string_stack.pop()

#             string_stack.append(res)

#     return ''.join(string_stack)

# print(decodeString(s))


def isMatch(s: str, p: str) -> bool:

    s_pointer = 0
    p_pointer = 0

    while s_pointer < len(s) or p_pointer < len(p):

        if (s_pointer < len(s) and p_pointer < len(p)) and (s[s_pointer] == p[p_pointer] or p[p_pointer] == '?'):

            s_pointer += 1
            p_pointer += 1

        elif p_pointer < len(p) and p[p_pointer] == "*":

            return True

        else:

            return False

    if s_pointer == len(s) - 1 and p_pointer == len(s) - 1:

        return True

    return False

s = "ho"
p = "**?ho"

print(isMatch(s,p))









    


