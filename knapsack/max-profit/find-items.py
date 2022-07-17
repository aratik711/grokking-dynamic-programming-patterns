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

‘22’ did not come from the top cell (which is 17); hence we must include the item at index ‘3’ (which is the item ‘D’).
Subtract the profit of item ‘D’ from ‘22’ to get the remaining profit ‘6’. We then jump to profit ‘6’ on the same row.
‘6’ came from the top cell, so we jump to row ‘2’.
Again, ‘6’ came from the top cell, so we jump to row ‘1’.
‘6’ is different than the top cell, so we must include this item (which is item ‘B’).
Subtract the profit of ‘B’ from ‘6’ to get the profit ‘0’. We then jump to profit ‘0’ on the same row. As soon as we hit zero remaining profit, we can finish our item search.
So items going into the knapsack are {B, D}.

"""
from __future__ import print_function

def solve_knapsack(profits, weights, capacity):
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    dp = [[ 0 for x in range(capacity + 1)] for y in range(n)]
    for c in range(capacity + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]
    for i in range(1,n):
        for c in range(1, capacity+1):
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                profit1 = profits[i] + dp[i-1][c-weights[i]]
            profit2 = dp[i-1][c]
            dp[i][c] = max(profit1,profit2)
    print_selected_elements(dp, weights, profits, capacity)
    return dp[n-1][capacity]

def print_selected_elements(dp, weights, profits, capacity):
    print("Selected weights are: ", end='')
    n = len(weights)
    totalProfit = dp[n-1][capacity]
    for i in range(n-1, 0, -1):
        if totalProfit != dp[i-1][capacity]:
            print(str(weights[i]) + " ", end='')
            capacity -= weights[i]
            totalProfit -= profits[i]
    if totalProfit != 0:
        print(str(weights[0]) + " ", end='')

def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))

main()
