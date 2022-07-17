"""

Given an infinite supply of ‘n’ coin denominations and a total money amount, we are asked to find the total number of distinct ways to make up that amount.

Example:

Denominations: {1,2,3}
Total amount: 5
Output: 5
Explanation: There are five ways to make the change for '5', here are those ways:
  1. {1,1,1,1,1}
  2. {1,1,1,2}
  3. {1,2,2}
  4. {1,1,3}
  5. {2,3}

The above solution has time and space complexity of O(C*T), where ‘C’ represents total coin denominations and ‘T’ is the total amount that we want to make change.


"""
def count_change(denominations, change):
    dp = [ [0 for x in range(change+1)] for y in range(len(denominations))]
    n = len(denominations)
    if n == 0:
        return 0
    for i in range(n):
        dp[i][0] = 1
    for i in range(n):
        for c in range(1, change + 1):
            if i > 0:
                dp[i][c] = dp[i-1][c]
            if denominations[i] <= c:
                dp[i][c] += dp[i][c - denominations[i]]
    return dp[n-1][change]

def main():
  print(count_change([1, 2, 3], 5))


main()
