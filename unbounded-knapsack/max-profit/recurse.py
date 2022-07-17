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

The time complexity of the above algorithm is exponential O(2^{N+C}), where ‘N’ represents the total number of items. The space complexity will be O(N+C)
 to store the recursion stack.


"""
def solve_knapsack(profits, weights, capacity):
    return solve_knapsack_recurse(profits, weights, capacity, 0)

def solve_knapsack_recurse(profits, weights, capacity, currentIndex):
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n or currentIndex >= n:
        return 0
    profit1 = 0
    if weights[currentIndex] <= capacity:
        profit1 = profits[currentIndex] + solve_knapsack_recurse(profits, weights, capacity - weights[currentIndex], currentIndex + 1)
    profit2 = solve_knapsack_recurse(profits, weights, capacity, currentIndex + 1)
    return max(profit1, profit2)



def main():
  print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 8))
  print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 6))


main()
