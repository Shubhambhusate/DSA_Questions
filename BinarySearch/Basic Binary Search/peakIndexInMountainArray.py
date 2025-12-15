def peakIndexInMountainArray(arr: list[int]) -> int:

    if len(arr) == 1:
        return arr[0]

    start = 0
    end = len(arr) - 1
    maxValue = -float('inf')
    index = len(arr)

    while start <= end:

        mid = start + (end - start) // 2

        if arr[mid] < arr[mid-1]:

            end = mid - 1
        
        else:

            start = mid + 1

    return start - 1



arr =[0,10,5,2]

print(peakIndexInMountainArray(arr))
