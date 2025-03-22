class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        complete_count = 0 

        # DFS로 연결 요소 탐색
        def dfs(node):
            stack = [node]
            nodes = set()
            edge_count = 0 

            while stack:
                cur = stack.pop()
                if cur in visited:
                    continue
                visited.add(cur)
                nodes.add(cur)
                edge_count += len(graph[cur]) 
                for neighbor in graph[cur]:
                    if neighbor not in visited:
                        stack.append(neighbor)

            V = len(nodes)
            E = edge_count // 2 

            if V * (V - 1) == 2 * E:
                return 1
            return 0

        # 모든 노드에 대해 DFS 수행
        for node in range(n):
            if node not in visited:
                complete_count += dfs(node)

        return complete_count