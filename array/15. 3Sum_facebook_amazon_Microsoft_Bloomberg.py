"""
Name: 15. 3Sum_facebook_amazon_Microsoft_Bloomberg.py
Author: bangrenc
Time: 22/1/2020 11:38 AM
"""

def ThreeSum(nums):
    if len(nums) < 3:
        return []
    #
    record = []
    nums.sort()

    for i in range(len(nums)):
        left = 0
        right = len(nums) - 1
        while left < right:
            if left == i:
                left += 1

            if right == i:
                right -= 1

            if left >= right:
                break
    #
            if nums[left] + nums[right] + nums[i] == 0:
                if sorted([nums[left], nums[right], nums[i]]) not in record:
                    record.append(sorted([nums[left], nums[right], nums[i]]))
                    left += 1
                else:
                    left += 1

            elif nums[left] + nums[right] + nums[i] > 0:
                right -= 1
            else:
                left += 1
    return record


    #查表法

    # dct = {}
    # for i,n in enumerate(nums):
    #     dct[n] = dct.get(n,0) + 1
    # test = {}
    # record = []
    #
    # for i in range(len(nums)):
    #     for k,n in enumerate(nums):
    #         dct[n] -= 1
    #
    #         if -nums[i] - n in test and k != i:
    #             if sorted([nums[i], n, -nums[i] - n]) not in record:
    #                 record.append(sorted([nums[i], n, -nums[i] - n]))
    #         test[n] = k
    # return record


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    # nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    # nums = [0,0]
    # nums = [-1, 0, 1, 0]
    print(ThreeSum(nums))









