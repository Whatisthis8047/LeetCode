class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel_to_bit = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

        bitmask = 0
        bitmask_map = {0: -1} 
        max_length = 0

        for i, char in enumerate(s):
            if char in vowel_to_bit:
                bitmask ^= (1 << vowel_to_bit[char])
            if bitmask in bitmask_map:
                max_length = max(max_length, i - bitmask_map[bitmask])
            else:
                bitmask_map[bitmask] = i
        
        return max_length