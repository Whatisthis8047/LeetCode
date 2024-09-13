class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix = [0] * (n + 1)
        res = []

        for i in range(n):
            prefix[i+1] = prefix[i] ^ arr[i]

        for q in queries:
            res.append(prefix[q[1] + 1] ^ prefix[q[0]])
            
        return res
        