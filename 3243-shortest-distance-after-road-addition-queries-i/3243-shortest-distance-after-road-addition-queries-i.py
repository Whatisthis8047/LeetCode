class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for i in range(n-1):
            graph[i].append(i + 1)

        res = []

        def bfs(graph, n):
            queue = deque([(0, 0)])
            visited = set([0])
            
            while queue:
                node, dist = queue.popleft()
                if node == n-1:
                    return dist
                    
                for next_node in graph[node]:
                    if next_node not in visited:
                        visited.add(next_node)
                        queue.append((next_node, dist + 1))

        for u, v in queries:
            graph[u].append(v)
            res.append(bfs(graph, n))

        return res
