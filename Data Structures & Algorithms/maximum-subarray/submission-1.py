class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        ma=float('-inf')
        s=0
        for i in range(len(nums)):
            # s+=nums[i]
            if s<0:
                s=0
            s+=nums[i]
            ma=max(ma,s)
        return ma

