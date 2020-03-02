"""
Name: 88_Merge_Sorted_Array_facebook_Microsoft_Bloomberg.py
Author: bangrenc
Time: 19/1/2020 12:03 AM
"""
def Merge_Sorted_Array(nums1,nums2):
    for i in nums2:
        nums1.append(i)

    result = []
    for i in nums1:
        if i:
            result.append(i)

    print(result)

    for i in range(1, len(result)):
        if result[i-1] > result[i]:
            result[i-1], result[i] = result[i], result[i-1]
    nums1 = result

    return result

if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    print(Merge_Sorted_Array(nums1, nums2))






