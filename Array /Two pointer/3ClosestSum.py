
arr = [-1,2,1,-4] 
target = 1

def threeSumClosest(arr,target):

    arr.sort()

    closest_sum = arr[0] + arr[1] + arr[2]

    for i in range(len(arr)-2):

        left = i + 1
        right = len(arr) - 1

        while left < right:

            current_sum = arr[i] + arr[left] + arr[right]

            if abs(current_sum - target ) < abs (closest_sum - target):

                closest_sum = current_sum

            if sum == target:

                left += 1
                right -= 1

            elif current_sum < target:

                left += 1

            else:

                right -= 1

    return closest_sum
            
            
print(threeSumClosest(arr,target))

