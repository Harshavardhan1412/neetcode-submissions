class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def day(w,weights):
            c=1
            x=0
            for i in weights:
                if x+i>w:
                    c+=1
                    x=0
                x+=i
            return c
        low=max(weights)
        high=sum(weights)
        while low<=high:
            mid=(low+high)//2
            x=day(mid,weights)
            if x<=days:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return low

