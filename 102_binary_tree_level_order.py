"""Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).ss"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        level_dictionary = {}

        def add_to_dict(node,level):
            if level in level_dictionary.keys():
                if node.left:
                    level_dictionary[level] = level_dictionary[level] + [node.left.val]
                if node.right:
                     level_dictionary[level] = level_dictionary[level] + [node.right.val]
            else:
                if node.left and node.right:
                    level_dictionary[level] = [node.left.val, node.right.val]
                elif node.left:
                    level_dictionary[level] = [node.left.val]
                elif node.right:
                    level_dictionary[level] = [node.right.val]
                
            
            if node.left:
                add_to_dict(node.left, level+1)
            if node.right:
                add_to_dict(node.right, level +1)

            
        if root:
            level_dictionary[0] = [root.val]
            add_to_dict(root,1)

        print (level_dictionary)

        dict_as_tuples = sorted([(k, v) for k, v in level_dictionary.items()], key = lambda x: x[0])

        #get [x.val for x in v] for each v

        return [x[1] for x in dict_as_tuples]


        

        
        

        