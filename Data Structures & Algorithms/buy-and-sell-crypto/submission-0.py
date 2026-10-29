class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxincome = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                income = prices[j]-prices[i]
                if prices[j]-prices[i]>maxincome:
                    maxincome = income
        return maxincome