class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        final=[]
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                l=j+1
                h=len(nums)-1
                while l<h:
                    res=nums[i]+nums[j]+nums[l]+nums[h]
                    if res==target:
                        if [nums[i],nums[j],nums[l],nums[h]] not in final:
                            final.append([nums[i],nums[j],nums[l],nums[h]])
                        l+=1
                        h-=1
                    elif res>target:
                        h-=1
                    else:
                        l+=1
        return list(final)
