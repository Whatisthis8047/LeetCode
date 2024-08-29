class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}

        def find(x):
            if parent.setdefault(x, x) != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for x, y in stones:
            union(x, y + 10001)

        return len(stones) - len({find(x) for x, y in stones})