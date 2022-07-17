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

The below algorithm’s time complexity is exponential O(2^n), where ‘n’ represents the total number of items. This can also be confirmed from the above recursion tree. As we can see that we will have a total of ‘31’ recursive calls – calculated through (2^n) + (2^n) - 1, which is asymptotically equivalent to O(2^n)

The space complexity is O(n). This space will be used to store the recursion stack. Since our recursive algorithm works in a depth-first fashion, which means, we can’t have more than ‘n’ recursive calls on the call stack at any time.

"""

def solve_knapsack(profits, weights, capacity):
    return knapsack_recurse(profits, weights, capacity, 0)

def knapsack_recurse(profits, weights, capacity, currentIndex):
    if capacity <= 0 or currentIndex >= len(profits):
        return 0

    # recursive call after choosing the element at the currentIndex
    # if the weight of the element at currentIndex exceeds the capacity, we  shouldn't process this
    profit1 = 0
    if weights[currentIndex] <= capacity:
        profit1 = profits[currentIndex] + knapsack_recurse(profits, weights, capacity - weights[currentIndex], currentIndex + 1)

    # recursive call after excluding the element at the currentIndex
    profit2 = knapsack_recurse(profits, weights, capacity, currentIndex + 1)
    return max(profit1, profit2)

def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))

main()
