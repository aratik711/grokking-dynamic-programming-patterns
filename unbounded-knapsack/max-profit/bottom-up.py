"""
Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack that has a capacity ‘C’. The goal is to get the maximum profit from the items in the knapsack. The only difference between the 0/1 Knapsack problem and this problem is that we are allowed to use an unlimited quantity of an item.

Let’s take the example of Merry, who wants to carry some fruits in the knapsack to get maximum profit. Here are the weights and profits of the fruits:

Items: { Apple, Orange, Melon }
Weights: { 1, 2, 3 }
Profits: { 15, 20, 50 }
Knapsack capacity: 5

Let’s try to put different combinations of fruits in the knapsack, such that their total weight is not more than 5.

5 Apples (total weight 5) => 75 profit
1 Apple + 2 Oranges (total weight 5) => 55 profit
2 Apples + 1 Melon (total weight 5) => 80 profit
1 Orange + 1 Melon (total weight 5) => 70 profit

This shows that 2 apples + 1 melon is the best combination, as it gives us the maximum profit and the total weight does not exceed the capacity.

Since our memoization array dp[profits.length][capacity+1] stores the results for all the subproblems, we can conclude that we will not have more than N*C
 subproblems (where ‘N’ is the number of items and ‘C’ is the knapsack capacity). This means that our time complexity will be O(N*C).

The above algorithm will be using O(N*C) space for the memoization array. Other than that we will use O(N)
 space for the recursion call-stack. So the total space complexity will be O(N*C + N), which is asymptotically equivalent to O(N*C).


"""
def solve_knapsack(profits, weights, capacity):
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    dp = [ [-1 for x in range(capacity + 1)] for y in range(len(profits))]
    # populate the capacity=0 columns
    for i in range(n):
        dp[i][0] = 0
    for i in range(n):
        for c in range(1, capacity + 1):
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                profit1 = profits[i] + dp[i-1][c-weights[i]]
            if i > 0:
                profit2 = dp[i-1][c]
            dp[i][c] = max(profit1, profit2)

    return dp[n-1][capacity]



def main():
  print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 8))
  print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 6))


main()
