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

The above solution is similar to the previous solution; the only difference is that we use i%2 instead of i and (i-1)%2 instead of i-1. This solution has a space complexity of O(2*C) = O(C), where ‘C’ is the knapsack’s maximum capacity.

This space optimization solution can also be implemented using a single array. It is a bit tricky though, but the intuition is to use the same array for the previous and the next iteration!

If you see closely, we need two values from the previous iteration: dp[c] and dp[c-weight[i]]

Since our inner loop is iterating over c:0-->capacity, let’s see how this might affect our two required values:

When we access dp[c], it has not been overridden yet for the current iteration, so it should be fine.
dp[c-weight[i]] might be overridden if “weight[i] > 0”. Therefore we can’t use this value for the current iteration.
To solve the second case, we can change our inner loop to process in the reverse direction: c:capacity-->0. This will ensure that whenever we change a value in dp[], we will not need it anymore in the current iteration.

"""

def solve_knapsack(profits, weights, capacity):
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    dp = [ [ 0 for x in range( capacity + 1) ]for y in range(2) ]
    for c in range(1, capacity + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]
    for i in range(1,n):
        for c in range(1, capacity+1):
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                profit1 = profits[i] + dp[(i-1)%2][c - weights[i]]
            profit2 = dp[(i-1)%2][c]
            dp[i%2][c] = max(profit1, profit2)

    return dp[(n-1)%2][capacity]


def main():
    print("Total knapsack profit: " +
        str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)))
    print("Total knapsack profit: " +
        str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6)))


main()
