class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        st_node = [0] * n
        for u, v in edges:
            st_node[v] += 1
        
        res = None
        for i in range(len(st_node)):
            if res == None and st_node[i] == 0:
                res = i
            elif st_node[i] == 0:
                return -1
        return res