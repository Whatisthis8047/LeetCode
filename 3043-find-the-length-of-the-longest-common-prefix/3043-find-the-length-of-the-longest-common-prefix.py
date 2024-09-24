class Node:
    def __init__(self):
        self.children = [None] * 10

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, num):
        node = self.root
        num_str = str(num)
        for digit in num_str:
            idx = int(digit)
            if not node.children[idx]:
                node.children[idx] = Node()
            node = node.children[idx]
    
    def find_longest_prefix(self, num):
        node = self.root
        num_str = str(num)
        len = 0

        for digit in num_str:
            idx = int(digit)
            if node.children[idx]:
                len += 1
                node = node.children[idx]
            else:
                break
        return len


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()

        for num in arr1:
            trie.insert(num)
        
        res = 0

        for num in arr2:
            length = trie.find_longest_prefix(num)
            res = max(res, length)
        
        return res
