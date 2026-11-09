class Solution:
    def climbStairs(self, n: int) -> int:
        def fib(dp,n):
            if n==0:
                return 0
            if n==1:
                return 1
            else:
                if n in dp:
                    return dp[n]
                dp[n]=fib(dp,n-1)+fib(dp,n-2)
                return dp[n]
        return fib({},n+1)