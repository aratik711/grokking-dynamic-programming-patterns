"""

We are given a ribbon of length ‘n’ and a set of possible ribbon lengths. We need to cut the ribbon into the maximum number of pieces that comply with the above-mentioned possible lengths. Write a method that will return the count of pieces.

Example 1:

n: 5
Ribbon Lengths: {2,3,5}
Output: 2
Explanation: Ribbon pieces will be {2,3}.
Example 2:

n: 7
Ribbon Lengths: {2,3}
Output: 3
Explanation: Ribbon pieces will be {2,2,3}.
Example 3:

n: 13
Ribbon Lengths: {3,5,7}
Output: 3
Explanation: Ribbon pieces will be {3,3,7}.

The above solution has time and space complexity of O(L*N), where ‘L’ represents total ribbon lengths and ‘N’ is the total length that we want to cut.

"""

import math


def count_ribbon_pieces(ribbonLengths, total):
    n = len(ribbonLengths)
    dp = [ [-math.inf for x in range(total + 1)]for y in range(n)]
    for i in range(n):
        dp[i][0] = 0
    for i in range(n):
        for t in range(1, total+1):
            if i > 0:
                dp[i][t] = dp[i-1][t]
            if t >= ribbonLengths[i] and dp[i][t-ribbonLengths[i]] != -math.inf:
                dp[i][t] = max(dp[i][t], dp[i][t-ribbonLengths[i]] + 1)
    return -1 if dp[n-1][total] == -math.inf else dp[n-1][total]

def main():
  print(count_ribbon_pieces([2, 3, 5], 5))
  print(count_ribbon_pieces([2, 3], 7))
  print(count_ribbon_pieces([3, 5, 7], 13))
  print(count_ribbon_pieces([3, 5], 7))


main()
