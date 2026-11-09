class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))  # ✅ Sort after removing duplicates
        if not nums:
            return 0
        count = 1
        max_count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
        return max(max_count, count)
