"""

Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.

Example 1:#
Input: {1, 1, 2, 3}, S=4
Output: 3
The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
Note that we have two similar sets {1, 3}, because we have two '1' in our input.
Example 2:#
Input: {1, 2, 7, 1, 5}, S=9
Output: 3
The given set has '3' subsets whose sum is '9': {2, 7}, {1, 7, 1}, {1, 2, 1, 5}

The time complexity of the above algorithm is exponential O(2^n), where ‘n’ represents the total number. The space complexity is O(n)
, this memory is used to store the recursion stack.



"""
def count_subsets(num, sum):
    n = len(num)
    dp = [ [-1 for x in range(sum+1)] for y in range(n) ]
    # populate the sum = 0 columns, as we will always have an empty set for zero sum
    for i in range(0,n):
        dp[i][0] = 1
    for s in range(1, sum+1):
        dp[0][s] = 1 if num[0] == s else 0
    for i in range(1, n):
        for s in range(1, sum+1):
            dp[i][s] = dp[i-1][s]
            if num[i] <= s:
                dp[i][s] += dp[i-1][s-num[i]]
    return dp[n-1][sum]


def main():
  print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
  print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
