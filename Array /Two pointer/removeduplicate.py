arr = [0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(arr):

        for i in range(len(arr)):

            left = i
            right = len(arr) - 1

            while left < right:

                if arr[left] != arr[right]:

                    right -= 1

                else:

                    arr.pop(right)

                    right -= 1

        return arr
        
print(removeDuplicates(arr))

