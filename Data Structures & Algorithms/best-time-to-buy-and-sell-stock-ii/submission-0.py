class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        prof = [0 for _ in range(len(prices))]
        for i in range(len(prices)-1):
            prof[i] = prices[i+1] - prices[i]
        for num in prof:
            if num>0 :
                res+=num
        return res