"""
Name: 125 Valid Palindrome_facebook_Microsoft_Uber.py
Author: bangrenc
Time: 19/1/2020 12:11 PM
"""
import re
def valid_Palin(s):
    if s == "" or len(s) == 1:
        return True

    s_lower = s.lower() #转小写
    s_lower = re.sub("[^a-z0-9]", "", s_lower) #去掉除字母和数字之外的其他数

    if len(s_lower) == 1 or len(s_lower) == 0: #长度为了1和0的值都return true
        return True

    if len(s_lower) == 2: #两个数值一样，return True
        if s_lower[0] == s_lower[1]:
            return True
        else:
            return False

    First = 0
    Last = len(s_lower)-1
    while First < Last:
        if s_lower[First] == s_lower[Last]:
            First += 1
            Last -= 1
            if First == Last: #数组个数是奇数
                return True
            elif First - 1 == Last: #数组个数是双数
                return True
        else:
            return False

if __name__ == '__main__':
    # s = "A man, a Plan, a canal: Panama"
    # s = "race a car"
    # s = ""
    # s = "aa"
    # s = "0P"
    s = "abba"
    print(valid_Palin(s))






