class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final=[]
        target=0
        for i in range(len(nums)-2):
            l=i+1
            h=len(nums)-1
            while l<h:
                res=nums[i]+nums[l]+nums[h]
                if res==target:
                    if [nums[i],nums[l],nums[h]] not in final:
                        final.append([nums[i],nums[l],nums[h]])
                    l+=1
                    h-=1
                elif res>target:
                    h-=1
                else:
                    l+=1
        return final
