class Node:
    def __init__(self):
        self.data = None
        self.children = {}
        self.p_count = 0

class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word):
        node = self.head
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
            node.p_count += 1
        node.data = string
    
    def get_score(self, word):
        node = self.head
        res = 0
        for char in word:
            node = node.children[char]
            res += node.p_count
        return res

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        res = []
        for word in words:
            res.append(trie.get_score(word))
        return res

