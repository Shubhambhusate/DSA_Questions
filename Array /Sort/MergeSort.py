nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3


# def merge(nums1, m, nums2, n) -> None:
#     """
#     Do not return anything, modify nums1 in-place instead.
#     """

#     i , j = 0, 0

#     while i < m and j < n:

#         if nums1[i] > nums2[j]:

#             nums1[i] , nums2[j] = nums2[j] , nums1[i] 

#             nums2.sort()

#             i += 1

#         else:

#             i += 1

#     while j < n :

#         if nums1[i] == 0:

#             nums1[i] = nums2[j]

#             i += 1 
#             j += 1

#     return nums1


def merge(nums1, m, nums2, n) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    i , j = m - 1, n  - 1

    k = m + n - 1

    while i >= 0 and j >= 0:

        if nums1[i] < nums2[j]:

            nums1[k] = nums2[j]

            j -= 1

            k -= 1

        else:

            nums1[k] = nums1[i]

            i -= 1

            k -= 1

    while j >= 0:

        nums1[k] = nums2[j]

        k -= 1
        j -= 1

    return nums1


print(merge(nums1, m, nums2, n))
        
