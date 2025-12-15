# Given an array of strings strs, group the anagrams together. You can return the answer in any order.


# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.


def groupAnagrams(strs):

    sorted_list = []

    for i in range(len(strs)):

        sorted_list.append(''.join(sorted(strs[i])))

    # [aet,aet,aet,ant,ant,abt]

    hash_map = {}

    for index in range(len(sorted_list)):

        strVal = sorted_list[index]

        if strVal in hash_map:
            
            hash_map[strVal].append(index)

        else:

            hash_map[strVal] = [index]

    res = []

    for value in hash_map.values():

        inner_list = []

        for item in value:

            inner_list.append(strs[item])

        res.append(inner_list)


    return res


strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs))
