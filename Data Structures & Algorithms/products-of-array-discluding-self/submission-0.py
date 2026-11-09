class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr1=[1]
        arr2=[1]
        for i in range(1,len(nums)):
            x=nums[i-1]*arr1[-1]
            arr1.append(x)
        # print(arr1)
        nums.reverse()
        # print(nums)
        for i in range(1,len(nums)):
            x=nums[i-1]*arr2[-1]
            arr2.append(x)
        arr2.reverse()
        res=[]
        for i in range(len(arr1)):
            res.append(arr1[i]*arr2[i])
        return res

