class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cash=0
        hold=-prices[0]
        for p in prices[1:]:
            prev_cash=cash
            prev_hold=hold

            cash=max(cash,prev_hold+p)
            hold=max(hold,prev_cash-p)
        return cash
