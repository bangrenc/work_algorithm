"""
Name: 438 Find All Anagrams in a String_amason.py
Author: bangrenc
Time: 20/1/2020 8:21 PM
"""

def findAllAnag(s,p):
    # lookup = list(p)
    # # print(sorted("dac"))
    # if ['a','b'] == ['b','a']:
    #     print("test")
    # record = []
    # j = 0
    # for k in range(len(s)):
    #     j = 0
    #     while s[k+j] in lookup:
    #         lookup.remove(s[k+j])
    #         if j+1 == len(p) and lookup==[]:
    #             record.append(k)
    #             break
    #         if len(s) - 1 == k: #以防最后一个字母还跑下去
    #             break
    #
    #         j += 1
    #         if j+k >= len(s):
    #             break
    #
    #     lookup = list(p)
    # return record

    ret = []
    ori_data = {} #p的值
    window = {} #窗口的值

    for c in p: #p字典的值 初始化都加1
        ori_data[c] = ori_data.get(c,0) + 1

    lenght, limit = len(p),len(s)
    left = right = 0

    while lenght < limit:
        c = s[right]
        if c in ori_data:
            window[c] = window.get(c,0) + 1 #有一样的值 就在窗口+1
            if right - left + 1 == lenght: #长度等于p的长度
                if ori_data == window: #窗口和p的值一样，就记录下来
                    ret.append(left)
                window[s[left]] -= 1 #记录完，去掉左边的值
                left += 1 #下一个
            right += 1
        else:
            right = left = right+1
            window.clear()

        if right >= limit:
            break

    return ret

if __name__ == '__main__':
    # s= "cbaebabacd"
    # p= "abc"
    # s = "abab"
    # p = "ab"
    s = "abacbabc"
    p = "abc"
    print(findAllAnag(s,p))




