# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.

# Note: The characters in the array beyond the returned length do not matter and should be ignored.


def compress(chars) -> int:

    hash_map = {}

    for char in chars:

        hash_map[char] = hash_map.get(char,0) + 1

    res = []

    for char in chars:

        if hash_map[char] == 1 and char not in res:

            res.append(char)

        elif char not in res:

            res.append(char)

            while hash_map[char] > 10:

                value = hash_map[char] // 10

                hash_map[char] = hash_map[char] % 10
                
                res.append(str(value))

            res.append(str(hash_map[char]))

    return res

chars = ["a","a","b","b","c","c","c"]

# print(compress(chars))

# Optimise solution 

def compressOptimmise(chars) -> int:

    left = 0

    groupLength = 1

    for right in range(1, len(chars)):

        if chars[right] == chars[right - 1]:

            groupLength += 1

        else:

            chars[left] = chars[right - 1]
            left += 1

            if groupLength > 1:

                for c in str(groupLength):

                    chars[left] = c

                    left += 1

            groupLength = 1

    chars[left] = chars[-1]

    left += 1

    if groupLength > 1:

        for c in str(groupLength):

            chars[left] = c

            left += 1

    return left , chars[:left]


print(compressOptimmise(chars))