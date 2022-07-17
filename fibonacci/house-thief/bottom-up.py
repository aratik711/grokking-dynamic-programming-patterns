"""

Given a number array representing the wealth of n houses, determine the maximum amount of money the thief can steal without alerting the security system.

Example 1:

Input: {2, 5, 1, 3, 6, 2, 4}
Output: 15
Explanation: The thief should steal from houses 5 + 6 + 4
Example 2:

Input: {2, 10, 14, 8, 1}
Output: 18
Explanation: The thief should steal from houses 10 + 8

The only restriction the thief has is that he can’t steal from two consecutive houses, as that would alert the security system. How should the thief maximize his stealing?

"""

def find_max_steal(wealth):
    dp = [0 for x in range(len(wealth) + 1)]
    n = len(wealth)
    if n == 0:
        return 0
    dp[0] = 0
    dp[1] = wealth[0]
    for i in range(1, n):
        dp[i+1] = max(wealth[i] + dp[i-1], dp[i])

    return dp[n]


def main():

  print(find_max_steal([2, 5, 1, 3, 6, 2, 4]))
  print(find_max_steal([2, 10, 14, 8, 1]))


main()
