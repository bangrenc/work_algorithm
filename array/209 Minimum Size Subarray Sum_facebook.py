"""
Name: 209 Minimum Size Subarray Sum_facebook.py
Author: bangrenc
Time: 19/1/2020 4:23 PM
"""

#滑动窗口，找出最小窗口
#时间复杂度O(n)。因为滑动窗口 维 数组绕了一圈
#空间复杂度O(1)。因为没有开辟新的数组
def Minimum_size(nums,s):
    l = 0
    r = -1 #[l,r]为滑动窗口
    sum_sub = 0
    res = len(nums) + 1

    while l < len(nums):
        if (r+1 < len(nums)) and sum_sub < s:
            r += 1
            sum_sub += nums[r]
        else:
            sum_sub -= nums[l]
            l += 1

        if sum_sub >= s:
            res = min(res, r-l+1)

        #等于1，也就是最小的，提前跳出来
        if res == 1:
            return 1

    if res == len(nums)+1:
        return 0
    else:
        return res

if __name__ == '__main__':
    nums = [5,1,3,5,10,7,4,9,2,8]
    s = 15
    print(Minimum_size(nums,s))




