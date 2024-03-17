import math
# A Naive recursive python program to find minimum of coins
# to make a given change V
 
import sys

from pip import main
 
# m is size of coins array (number of different coins)
def minCoins(coins, m, V):
 
    # base case
    if (V == 0):
        return 0
 
    # Initialize result
    res = sys.maxsize
     
    # Try every coin that has smaller value than V
    for i in range(0, m):
        if (coins[i] <= V):
            sub_res = minCoins(coins, m, V-coins[i])
 
            # Check for INT_MAX to avoid overflow and see if
            # result can minimized
            if (sub_res != sys.maxsize and sub_res + 1 < res):
                res = sub_res + 1
 
    return res
 
# Driver program to test above function
coins = [9, 6, 5, 1]
m = len(coins)
V = 11
print("Minimum coins required is",minCoins(coins, m, V))
 
# This code is contributed by
# Smitha Dinesh Semwal


def foo_all(amount, coins):
    dp = [0]*(amount+1)
    dp[0] = 1

    for i in range (len(coins)-1,-1,-1):
        nextDP = [0]* (amount+1)
        nextDP[0] = 1

        for a in range(1, amount+1):
            nextDP[a] = dp[a]
            if a - coins[i] >= 0:
                nextDP[a] += nextDP[a-coins[i]]
        dp = nextDP
    return dp


if __name__=="__main__":
    coin_values = [1,5,10,25]
    coin_limit = [3,2,1,1]
    amount = 13
    dp = [0]*(amount+1)
    dp[0] = 1

    for a in range(1, amount+1):
        for c in coin_values:
            if a - c >= 0:
                #print("dp[a]",dp[a])
                dp[a] = max(dp[a], 1+dp[a-c])
    print(dp[amount]) if dp[amount] == (amount+1) else print("impossible")

    print("ALL: ", foo_all(amount,coin_values))




