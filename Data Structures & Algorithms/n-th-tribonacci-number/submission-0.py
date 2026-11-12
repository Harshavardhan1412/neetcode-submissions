class Solution:
    def tribonacci(self, n: int) -> int:
        def fib(memo,n):
            if n==0:
                return 0
            if n==1 or n==2:
                return 1
            if n in memo:
                return memo[n]
            memo[n]=fib(memo,n-1)+fib(memo,n-2)+fib(memo,n-3)
            return memo[n]
        return fib({},n)