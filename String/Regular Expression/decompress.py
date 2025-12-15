# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. 
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"

s = "2[abc]3[cd]ef"

def decompress(s):

    string_stack = []
    number_stack = []
    num = ""

    for i in range(len(s)):

        char = s[i]

        if char.isdigit():

            num += char

            if i + 1 < len(s) or not s[i+1].isdigit():

                number_stack.append(int(num))

                num = ""

        elif char.isalpha() or char == "[":

            string_stack.append(char)

        elif char == ']':

            res = ''

            while string_stack[-1] != '[':

                res = string_stack.pop() + res

            string_stack.pop()

            res = res * number_stack.pop()

            string_stack.append(res)

    return ''.join(string_stack)

print(decompress(s))





             
