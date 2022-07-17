"""

Given a stair with ‘n’ steps, implement a method to count how many possible ways are there to reach the top of the staircase, given that, at every step you can either take 1 step, 2 steps, or 3 steps.

Example 1:

Number of stairs (n) : 3
Number of ways = 4
Explanation: Following are the four ways we can climb : {1,1,1}, {1,2}, {2,1}, {3}
Example 2:

Number of stairs (n) : 4
Number of ways = 7
Explanation: Following are the seven ways we can climb : {1,1,1,1}, {1,1,2}, {1,2,1}, {2,1,1},
{2,2}, {1,3}, {3,1}

Since our memoization array dp[n+1] stores the results for all the subproblems, we can conclude that we will not have more than n+1
 subproblems (where ‘n’ represents the total number of steps). This means that our time complexity will be O(N)
. The space complexity will also be O(n) this space will be used to store the recursion-stack.



"""

def count_ways(n):
    dp = [ 0 for i in range(n + 1)]
    return count_ways_recurse(n, dp)

def count_ways_recurse(n, dp):
    if n <= 1:
        return 1
    if n == 2:
        return 2
    if dp[n] == 0:
        count1 = count_ways_recurse(n-1, dp)
        count2 = count_ways_recurse(n-2, dp)
        count3 = count_ways_recurse(n-3, dp)
        dp[n] = count1 + count2 + count3
    return dp[n]


def main():

  print(count_ways(3))
  print(count_ways(4))
  print(count_ways(5))


main()
