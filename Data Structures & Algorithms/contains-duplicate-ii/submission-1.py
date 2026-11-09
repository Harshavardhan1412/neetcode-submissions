class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        flag=0
        for i in range(len(nums)):
            if nums[i] in d:
                if abs(i-d[nums[i]][-1])<=k:
                    flag=1
                d[nums[i]].append(i)
            else:
                d[nums[i]]=[i]
        print(d)
        if flag==1:
            return True
        return False