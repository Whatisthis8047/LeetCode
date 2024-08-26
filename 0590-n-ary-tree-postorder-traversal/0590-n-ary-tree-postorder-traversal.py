"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def _traverse(self, node, res):
        for child in node.children:
            self._traverse(child, res)
            res.append(child.val)
            
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        self._traverse(root, res)
        res.append(root.val)
        return res
        

            