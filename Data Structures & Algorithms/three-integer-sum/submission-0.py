class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=[]
        nums.sort()
        n=len(nums)
        for i in range(n-2):
            start=i+1
            end=n-1
            while start<end:
                if nums[i]+nums[start]+nums[end]==0:
                    if [nums[i],nums[start],nums[end]] not in l:
                        l.append([nums[i],nums[start],nums[end]])
                    start+=1
                    end-=1
                elif nums[i]+nums[start]+nums[end]<0:
                    start+=1
                else:
                    end-=1
            # print(l)
        return l