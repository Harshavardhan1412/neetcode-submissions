class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left=0
        right=len(arr)-k
        while left<right:
            mid=(left+right)//2
            a=arr[mid]
            b=arr[mid+k]
            if abs(a-x)<abs(b-x):
                right=mid
            elif abs(a-x)>abs(b-x):
                left=mid+1
            else:
                if a<b:
                    right=mid
                else:
                    left=mid+1
        return arr[left:left+k]
