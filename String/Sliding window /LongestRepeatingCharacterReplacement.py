# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:

# Input: s = "AABABBA", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Non optimal approach because we have creating all the possible substring time complexity is O(N^2) and space required arr[26]

def characterReplacement( s: str, k: int):

    max_length = 0

    max_frequency = 0

    for i in range(len(s)):

        arr = [0] * 26

        for j in range(i, len(s)):

            char = s[j]

            index = ord(char) - ord('A')

            arr[index] += 1

            max_frequency = max (max_frequency, max(arr))

            if j - i + 1 - max_frequency <= k:

                max_length = max(max_length, j - i + 1)
            
            else:

                break

    return max_length 

s = "AABABBA"
k = 2

print(characterReplacement( s, k))


def characterReplacementOptimal( s: str, k: int):

    max_length = 0

    max_frequency = 0

    arr = [0] * 26

    left = 0

    for right in range(len(s)):

        char = s[right]

        index = ord(char) - ord('A')

        arr[index] += 1

        max_frequency = max(max_frequency, max(arr))

        while right - left + 1 - max_frequency > k:

            char2 = s[left]

            index2 = ord(char2) - ord('A')

            arr[index2] -= 1

            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

print(characterReplacementOptimal( s, k))





            

