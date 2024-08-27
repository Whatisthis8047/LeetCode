class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i, (start, end) in enumerate(edges):
            graph[start].append([end, succProb[i]])
            graph[end].append([start, succProb[i]])
        
        prob = [0.0] * n
        prob[start_node] = 1.0

        queue = deque([start_node])
        while queue:
            cur_node = queue.popleft()
            for nxt_node, path_prob in graph[cur_node]:
                if prob[cur_node] * path_prob > prob[nxt_node]:
                    prob[nxt_node] = prob[cur_node] * path_prob
                    queue.append(nxt_node)

        return prob[end_node]