class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        st_node = [0] * n
        for u, v in edges:
            st_node[v] = 1
        
        if st_node.count(0) == 1:
            return st_node.index(0)
        return -1