class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr1,arr2):
            i,j=0,0
            res=[]
            while i<len(arr1) and j<len(arr2):
                if arr1[i]<=arr2[j]:
                    res.append(arr1[i])
                    i+=1
                else:
                    res.append(arr2[j])
                    j+=1
            while i<len(arr1):
                res.append(arr1[i])
                i+=1
            while j<len(arr2):
                res.append(arr2[j])
                j+=1
            return res
        def mergesort(arr,l,h):
            if l==h:
                return [arr[l]]
            mid=(l+h)//2
            left=mergesort(arr,l,mid)
            right=mergesort(arr,mid+1,h)
            return merge(left,right)
        return mergesort(nums,0,len(nums)-1)