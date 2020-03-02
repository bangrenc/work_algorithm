"""
Name: 215 Kth Largest Element in an Array_facebook_Microsoft_amason_Bloomberg_Apple.py
Author: bangrenc
Time: 19/1/2020 12:20 AM
"""

def Kth_largest_Element_in_an_Array(nums, k):
    nums = sorted(nums)
    print(nums)
    result = nums[-k]
    print(result)

if __name__ == '__main__':
    nums = [3,2,1,5,6,4] #[3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 2
    print(Kth_largest_Element_in_an_Array(nums, k))



