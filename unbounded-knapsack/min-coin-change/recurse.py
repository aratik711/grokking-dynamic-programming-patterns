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

The time complexity of the above algorithm is exponential O(2^{C+T}), where ‘C’ represents total coin denominations and ‘T’ is the total amount that we want to make change. The space complexity will be O(C+T)

"""

import math


def count_change(denominations, total):
    result = count_change_recurse(denominations, total, 0)
    return -1 if result == math.inf else result

def count_change_recurse(denominations, total, currentIndex):
    n = len(denominations)
    if n == 0 or currentIndex >= n:
        return math.inf
    if total == 0:
        return 0
    count1 = math.inf
    if denominations[currentIndex] <= total:
        res = count_change_recurse(denominations, total - denominations[currentIndex], currentIndex)
        if res != math.inf:
            count1 = res + 1
    count2 = count_change_recurse(denominations, total, currentIndex + 1)
    return min(count1, count2)


def main():
  print(count_change([1, 2, 3], 5))
  print(count_change([1, 2, 3], 11))
  print(count_change([1, 2, 3], 7))
  print(count_change([3, 5], 7))


main()
