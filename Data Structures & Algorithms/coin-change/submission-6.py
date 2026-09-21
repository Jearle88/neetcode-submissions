class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount==0:
            return 0
        
        dp=[99999]*(amount+1)

        n=len(coins)
        # count up, search for the min amount of coins at each number leading up to the amount
        for curr_amount in range(amount+1):

            for j in range(n-1,-1,-1):
                if coins[j]>curr_amount:
                    continue
                if coins[j]==curr_amount:
                    dp[curr_amount]=1
                else:
                    dp[curr_amount]= min(dp[curr_amount],dp[curr_amount-coins[j]]+1)
        #print(dp)
       
        if dp[-1]==99999:
            return -1
        return dp[-1]

                




