class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        count = Counter(s)
        
        odd_count = sum(1 for c in count.values() if c % 2 != 0)
        
        return odd_count <= k <= len(s) 