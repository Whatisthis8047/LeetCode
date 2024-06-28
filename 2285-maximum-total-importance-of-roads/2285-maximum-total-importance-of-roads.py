class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        appear = [0] * n
        for u, v in roads:
            print(u,v)
            appear[u] += 1
            appear[v] += 1
        appear.sort()
        res = 0
        for i in range(1, n+1):
            res += i * appear[i-1]
        return res