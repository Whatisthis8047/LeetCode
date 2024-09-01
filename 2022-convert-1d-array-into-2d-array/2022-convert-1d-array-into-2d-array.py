class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []

        res = [[] for _ in range(m)]
        track_m, track_n = 0, 0 
        for i in range(len(original)):
            if track_n < n:
                res[track_m].append(original[i])
                track_n += 1
                
            elif track_n >= n:
                track_m += 1
                res[track_m].append(original[i])
                track_n = 1
        return res