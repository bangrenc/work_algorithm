"""
Name: 1. Two Sum.py
Author: bangrenc
Time: 21/1/2020 11:33 AM
"""
#哈希算法
#通过哈希来求解，这里通过字典来模拟哈希查询的过程
def twoSum(nums,target):
    # hashmap = {}
    # for ind,num in enumerate(nums):
    #     hashmap[num] = ind
    #
    # for i,num in enumerate(nums):
    #     j = hashmap.get(target-num)
    #     if j is not None and i!=j:
    #         return [i,j]

    #查找表法
    dct = {}
    for i, n in enumerate(nums): #i是序列号，n是序列号对应的号码
        if target - n in dct: #因为n是在变化的，每次和target相减 对比之前的值
            return [dct[target - n], i] #dct[target - n]之前的序列号，i是这次的
        dct[n] = i #把之前的存入dct
        # print(dct)

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 13
    print(twoSum(nums,target))


