class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # solving with sliding window technique
        max_num = max(nums)
        res, temp = 0, 0
        for i in range(nums.index(max_num), len(nums)):
            if nums[i] == max_num:
                temp += 1
            else:
                res = max(res, temp)
                temp = 0
        res = max(res, temp)
        return res