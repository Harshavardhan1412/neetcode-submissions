class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        else:
            s=0
            left=0
            right=0
            m=float('inf')
            while right<len(nums):
                s+=nums[right]
                while s>=target:
                    m=min(m,right-left+1)
                    s-=nums[left]
                    left+=1
                right+=1
            return m
