"""
Name: 167 Two Sum II - Input array is sorted_amason.py
Author: bangrenc
Time: 19/1/2020 10:29 AM
"""

def Two_Sum2(numbers,target):
    #暴力解法
    # result = []
    # for i in range(len(numbers) - 1):
    #     for j in range(1+i,len(numbers)):
    #         if numbers[i] + numbers[j] == target:
    #             result.append(i+1)
    #             result.append(j+1)
    #             return result


    #Binary search二分查找法。在有序的情况下 可以用二分查找法
    #时间复杂度为O(nlogn)，外面for循环是n，里面while循环是logn，比上面的暴力解法O(n^2)高效
    # record = []
    # for i in range(len(numbers)):
    #     result = target - numbers[i]
    #
    #     Fir = 0
    #     Last = len(numbers) - 1  # 范围在Fir =0和 Last之间
    #     while Fir <= Last:
    #         mid = int((Fir + Last) / 2)
    #
    #         if numbers[mid] == result:
    #             if mid != i:
    #                 record.append(i+1)
    #                 record.append(mid+1)
    #                 return sorted(record)
    #
    #         if numbers[mid] < result:
    #             Fir = mid + 1
    #         else:
    #             Last = mid - 1


    #对撞指针，有序数组的条件下
    #对比俩边和target的大小，两边的数值向中间偏移
    #时间复杂度O(n)
    #空间复杂度O(1)
    result = []
    Fir = 0
    Last = len(numbers) - 1  # 范围在Fir 和 Last之间
    while Fir < Last:
        if numbers[Fir] + numbers[Last] == target:
            result.append(Fir+1)
            result.append(Last+1)
            return result

        if numbers[Fir] + numbers[Last] < target:
            Fir += 1
        else:
            Last -= 1

if __name__ == '__main__':
    numbers = [5,25,75]
    target = 100
    print(Two_Sum2(numbers,target))




