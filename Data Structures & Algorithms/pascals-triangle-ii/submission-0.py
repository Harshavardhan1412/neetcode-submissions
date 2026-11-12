class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n=rowIndex
        dp=[[-1]*(n+1) for _ in range(n+1)]
        dp[0]=[1]
        for i in range(1,n+1):
            for j in range(i+1):
                if j==0 or j==i:
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
        return dp[n]

        