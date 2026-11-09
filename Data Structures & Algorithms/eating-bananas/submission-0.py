class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int: 
        def hours(a,h):
            t=0
            for i in a:
                t+=math.ceil(i/h)
            return t 
        low=1
        high=max(piles)
        ans=float('inf')
        while low<=high:
            mid=(low+high)//2
            total=hours(piles,mid)
            if total<=h:
                high=mid-1
                ans=min(ans,mid)
            else:
                low=mid+1
        return ans