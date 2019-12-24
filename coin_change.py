class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        memo = [0] * (amount + 1)
        if amount == 0:
            return 0
        
        def getChange(coins, amount):
            if amount < 0:
                return -1
            if amount == 0:
                return 0
            if memo[amount] != 0: return memo[amount]
            minval = float('inf')
            for coin in coins:
                res = getChange(coins, amount - coin)
                if res >= 0 and res < minval:
                    minval = 1 + res
            memo[amount] = -1 if minval == float('inf') else minval
            return memo[amount]
        return getChange(coins, amount)
                
            
        