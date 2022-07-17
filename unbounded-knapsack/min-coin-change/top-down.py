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

"""

import math


def count_change(denominations, total):
    dp = [ [-1 for x in range(total + 1)] for y in range(len(denominations))]
    result = count_change_recurse(denominations, total, 0, dp)
    return -1 if result == math.inf else result

def count_change_recurse(denominations, total, currentIndex, dp):
    n = len(denominations)
    if n == 0 or currentIndex >= n:
        return math.inf
    if total == 0:
        return 0
    if dp[currentIndex][total] == -1:
        count1 = math.inf
        if denominations[currentIndex] <= total:
            res = count_change_recurse(denominations, total - denominations[currentIndex], currentIndex, dp)
            if res != math.inf:
                count1 = res + 1
        count2 = count_change_recurse(denominations, total, currentIndex + 1, dp)
        dp[currentIndex][total] = min(count1, count2)
    return dp[currentIndex][total]

def main():
  print(count_change([1, 2, 3], 5))
  print(count_change([1, 2, 3], 11))
  print(count_change([1, 2, 3], 7))
  print(count_change([3, 5], 7))


main()
