class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        right=len(matrix)-1
        while(left<=right):
            mid=(left+right)//2
            if target in matrix[mid]:
                return True
            elif matrix[mid][0]>target:
                right-=1
            else:
                left+=1
        return False
        