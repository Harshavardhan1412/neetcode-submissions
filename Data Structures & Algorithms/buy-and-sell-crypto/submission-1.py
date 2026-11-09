class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        cur=prices[0]
        for i in range(1,len(prices)):
            m=max(m,prices[i]-cur)
            if prices[i]<cur:
                cur=prices[i]
        return m