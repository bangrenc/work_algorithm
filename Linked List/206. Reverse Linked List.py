"""
Name: 206. Reverse Linked List.py
Author: bangrenc
Time: 29/1/2020 10:33 AM
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(head):
        if not head:
            return prev
        next = head.next
        head.next = prev
        return self.reverseList(next, head)


if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    head = ListNode(head)
    test = Solution
    print(test.reverseList(head))

