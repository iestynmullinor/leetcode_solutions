"""Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def get_kids(node):
            vals=[]

            if node.children:
                kids = node.children
                for kid in kids:
                    vals.append(kid.val)
                    vals = vals + get_kids(kid)

            return vals
            
        pre_order=[]
        if root:
            pre_order = [root.val] + get_kids(root)

        return pre_order

        
