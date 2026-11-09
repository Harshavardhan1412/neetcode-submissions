class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        start=0
        l=1
        for i in range(n):
            dp[i][i]=True
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                if l<2:
                    l=2
                    start=i
        for i in range(3,n+1):
            for j in range(n-i+1):
                k=j+i-1
                if dp[j+1][k-1] and s[j]==s[k]:
                    dp[j][k]=True
                    if l<i:
                        l=i
                        start=j
        return s[start:start+l]