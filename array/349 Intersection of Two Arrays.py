"""
Name: 349 Intersection of Two Arrays.py
Author: bangrenc
Time: 21/1/2020 10:40 AM
"""

def inter_two_Arrays(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    record = []

    for i in nums1:
        if i in nums2:
            record.append(i)
    return record

if __name__ == '__main__':
    # nums1 = [1, 2, 2, 1]
    # nums2 = [2, 2]
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(inter_two_Arrays(nums1,nums2))

