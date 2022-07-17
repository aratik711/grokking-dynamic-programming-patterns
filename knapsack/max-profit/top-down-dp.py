"""
Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack that has a capacity ‘C’. The goal is to get the maximum profit from the items in the knapsack. Each item can only be selected once, as we don’t have multiple quantities of any item.

Let’s take Merry’s example, who wants to carry some fruits in the knapsack to get maximum profit. Here are the weights and profits of the fruits:

Items: { Apple, Orange, Banana, Melon }
Weights: { 2, 3, 1, 4 }
Profits: { 4, 5, 3, 7 }
Knapsack capacity: 5

Let’s try to put different combinations of fruits in the knapsack, such that their total weight is not more than 5:

Apple + Orange (total weight 5) => 9 profit
Apple + Banana (total weight 3) => 7 profit
Orange + Banana (total weight 4) => 8 profit
Banana + Melon (total weight 5) => 10 profit

This shows that Banana + Melon is the best combination, as it gives us the maximum profit and the total weight does not exceed the capacity.

Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C’. Write a function that returns the maximum profit. Each item can only be selected once, which means either we put an item in the knapsack or skip it.

Since our memoization array dp[profits.length][capacity+1] stores the results for all the subproblems, we can conclude that we will not have more than N*C subproblems
The below algorithm will be using O(N*C) space for the memoization array. Other than that, we will use O(N) space for the recursion call-stack. So the total space complexity will be O(N*C + N)
 which is asymptotically equivalent to O(N*C)

"""

def solve_knapsack(profits, weights, capacity):
    dp = [[-1 for x in range(capacity+1)]for y in range(len(profits))]
    return knapsack_dp(profits, weights, capacity, 0 , dp)

def knapsack_dp(profits, weights, capacity, currentIndex, dp):
    if capacity <= 0 or currentIndex >= len(profits):
        return 0
    if dp[currentIndex][capacity] != -1:
        return dp[currentIndex][capacity]
    profit1 = 0
    if weights[currentIndex] <= capacity:
        profit1 = profits[currentIndex] + knapsack_dp(profits, weights, capacity - weights[currentIndex], currentIndex + 1, dp)
    profit2 = knapsack_dp(profits, weights, capacity, currentIndex + 1, dp)

    dp[currentIndex][capacity] = max(profit1, profit2)
    return dp[currentIndex][capacity]

def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))

main()
