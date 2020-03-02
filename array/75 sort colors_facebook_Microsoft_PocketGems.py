"""
Name: sort_colors_facebook_Microsoft_PocketGems.py
Author: bangrenc
Time: 18/1/2020 8:22 PM
"""

#计数排序：分别统计0，1，2的元素个数，再填补每个元素的个数到新大数组里面
# 时间复杂度O(n)，因为只是循环nums里面的数据
# 空间复杂度O(k)，因为下面只是开了3个空间
# def sort_colors(nums):
#     result = [0 for i in range(3)]
#     # print(result)
#
#     for i in nums:
#         result[i] += 1
#
#     final_result = []
#
#     for i in range(result[0]):
#         final_result.append(0)
#     for i in range(result[1]):
#         final_result.append(1)
#     for i in range(result[2]):
#         final_result.append(2)
#
#     return final_result


#三路快排
#时间复杂度：O(n)
#空间复杂度：O(1)
#只需要变量一遍
def sortColors(nums):
    zero = -1
    two = len(nums)

    i = 0
    while i < two:
        if nums[i] == 1:
            i += 1
        elif nums[i] == 2:
            two -= 1
            nums[i], nums[two] = nums[two], nums[i] #两边互换
        else:
            assert nums[i] == 0
            zero += 1
            nums[zero], nums[i] = nums[i], nums[zero] #等于0，两边互换
            i += 1

    return nums

if __name__ == '__main__':
    nums = [1,2,1,0,0,0,2,1,2,1,2,2,2]
    print(sortColors(nums))








