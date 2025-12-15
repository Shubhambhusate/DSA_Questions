# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

def findSmallestLetterGreaterThanTarget(letters, target):

    start = 0
    end = len(letters) - 1

    while start <= end:

        mid = start + (end - start) // 2

        if letters[mid] > target:

            end = mid - 1

        else:

            start = mid + 1

    return letters[start] if start < len(letters) else letters[0]


letters = ["c","f","j"]
target = "a"
print(findSmallestLetterGreaterThanTarget(letters,target))
