"""Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list."""

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        current_node = head
        d = {}
        pos = 0
        prev_node = current_node
        while (not current_node in d) and (current_node):
            d[current_node] = pos
            pos+=1
            prev_node = current_node
            current_node = current_node.next

        if prev_node in d:
            return current_node
        else:
            return None
        

        
        