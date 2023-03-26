# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        current_node = head
        nodes = []
        while current_node:
            nodes.append(current_node)
            current_node = current_node.next

        return nodes[int((len(nodes))/2+1) - 1]
