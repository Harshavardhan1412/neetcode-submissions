class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==0:
            return []
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l=[]
        sorted_dict = list(dict(sorted(d.items(), key=lambda item: item[1], reverse=True)).keys())
        i=0
        while k:
            l.append(sorted_dict[i])
            k-=1
            i+=1
        return l

