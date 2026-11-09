class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        mi=float('inf')
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            mi=min(nums[mid],mi)
            if nums[l]<nums[mid]:
                mi=min(nums[l],mi)
                l=mid+1
            else:
                mi=min(nums[r],mi)
                r=mid-1
        return mi
