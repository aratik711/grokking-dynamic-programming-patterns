"""

Given an infinite supply of ‘n’ coin denominations and a total money amount, we are asked to find the minimum number of coins needed to make up that amount.

Example 1:

Denominations: {1,2,3}
Total amount: 5
Output: 2
Explanation: We need a minimum of two coins {2,3} to make a total of '5'
Example 2:

Denominations: {1,2,3}
Total amount: 11
Output: 4
Explanation: We need a minimum of four coins {2,3,3,3} to make a total of '11'

The above solution has time and space complexity of O(C*T)
, where ‘C’ represents total coin denominations and ‘T’ is the total amount that we want to make change.

"""

import math


def count_change(denominations, total):
    dp = [ [math.inf for x in range(total + 1)] for y in range(len(denominations))]
    n = len(denominations)
    for i in range(n):
        dp[i][0] = 0
    for i in range(n):
        for t in range(1, total+1):
            if i > 0:
                dp[i][t] = dp[i-1][t]
            if denominations[i] <= t:
                if dp[i][t - denominations[i]] != math.inf:
                    dp[i][t] = min(dp[i][t], dp[i][t-denominations[i]] + 1)
    return -1 if dp[n-1][total] == math.inf else dp[n-1][total]

def main():
  print(count_change([1, 2, 3], 5))
  print(count_change([1, 2, 3], 11))
  print(count_change([1, 2, 3], 7))
  print(count_change([3, 5], 7))


main()
