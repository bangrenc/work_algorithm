"""
Name: 219. Contains Duplicate II_airbnd_Palantir.py
Author: bangrenc
Time: 27/1/2020 3:39 PM
"""

#时间复杂度O(n)
#空间复杂度O(k)
def contains_duplicate(nums, k):
    record = {}

    for i, num in enumerate(nums): #查表法
        if nums[i] in record:
            return True

        record[num] = i #把值记录起来

        print(record)
        if len(record) == k+1: #保持record中最多只有k个值
            record.pop(nums[i-k])

    return False





if __name__ == '__main__':
    nums = [1,2,3,1,2,3]
    k = 2
    print(contains_duplicate(nums,k))






