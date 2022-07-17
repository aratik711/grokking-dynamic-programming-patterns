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


The time complexity of the above algorithm is exponential O(2^{C+T}), where ‘C’ represents total coin denominations and ‘T’ is the total amount that we want to make change. The space complexity will be O(C+T)

"""
def count_change(denominations, change):
    return count_change_recurse(denominations, change, 0)

def count_change_recurse(denominations, change, currentIndex):
    n = len(denominations)
    if change == 0:
        return 1
    if n == 0 or currentIndex >= n:
        return 0
    sum1 = 0
    if denominations[currentIndex] <= change:
        sum1 = count_change_recurse(denominations, change - denominations[currentIndex], currentIndex)
    sum2 = count_change_recurse(denominations, change, currentIndex + 1)
    return sum1 + sum2

def main():
  print(count_change([1, 2, 3], 5))


main()
