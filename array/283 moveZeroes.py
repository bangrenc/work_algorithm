"""
Name: test.py
Author: bangrenc
Time: 18/1/2020 8:04 PM
"""
#把全部不为0的数拿出来，再补上0的个数
#时间复杂度O(n)
#空间复杂度O(n)
def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    result = []
    for i in nums:
        if i:
            result.append(i)

    for i in range(len(result), len(nums)):
        result.append(0)
    nums = result
    return nums

if __name__ == '__main__':
    nums = [0,1,0,3,0,13,12]
    print(moveZeroes(nums))





