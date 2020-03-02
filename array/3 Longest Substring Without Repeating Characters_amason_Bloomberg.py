"""
Name: 3 Longest Substring Without Repeating Characters_amason_Bloomberg.py
Author: bangrenc
Time: 19/1/2020 5:34 PM
"""
#滑动窗口
def Longest_sub(s):
    if not s:
        return 0

    lookup = set()
    left = 0
    max_len = 0
    cur_len = 0 #记录当前的长度

    for i in range(len(s)):
        cur_len += 1

        while s[i] in lookup: #循环 直到除去一样的单词为止
            lookup.remove(s[left]) #除去左边的单词
            left += 1
            cur_len -= 1

        if cur_len > max_len:
            max_len = cur_len

        lookup.add(s[i]) #加单词

    return max_len

if __name__ == '__main__':
    s = "abcbbcbb"
    print(Longest_sub(s))
