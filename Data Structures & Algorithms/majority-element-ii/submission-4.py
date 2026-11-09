class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums)<=2:
            return nums
        d={}
        res=set()
        n=len(nums)
        for i in nums:
            if i in d:
                d[i]+=1
                if d[i]>n//3:
                    res.add(i)
            else:
                d[i]=1
        return list(res)