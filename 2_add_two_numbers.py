# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_vals = [str(l1.val)]
        l2_vals = [str(l2.val)]

        l1_current = l1.next
        while l1_current:
            l1_vals.append(str(l1_current.val))
            l1_current = l1.next
        
        l2_current = l2.next
        while l2_current:
            l2_vals.append(str(l2_current.val))
            l2_current = l2.next

        l1_vals = l1_vals[::-1]
        l2_vals = l2_vals[::-1]
        sum = l1_vals + l2_vals

        result = []
        for number in str(sum):
            result





