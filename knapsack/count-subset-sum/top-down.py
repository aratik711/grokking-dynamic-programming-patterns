"""

Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number āSā.

Example 1:#
Input: {1, 1, 2, 3}, S=4
Output: 3
The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
Note that we have two similar sets {1, 3}, because we have two '1' in our input.
Example 2:#
Input: {1, 2, 7, 1, 5}, S=9
Output: 3
The given set has '3' subsets whose sum is '9': {2, 7}, {1, 7, 1}, {1, 2, 1, 5}

The time complexity of the above algorithm is exponential O(2^n), where ānā represents the total number. The space complexity is O(n)
, this memory is used to store the recursion stack.



"""
def count_subsets(num, sum):
    dp = [ [-1 for x in range(sum+1)] for y in range(len(num)) ]
    return count_subsets_recursive(num, sum, 0, dp)

def count_subsets_recursive(num, sum, currentIndex, dp):
    if sum == 0:
        return 1
    n = len(num)
    if n == 0 or currentIndex >= len(num):
        return 0
    if dp[currentIndex][sum] == -1:
        sum1 = 0
        if num[currentIndex] <= sum:
            sum1 = count_subsets_recursive(num, sum - num[currentIndex], currentIndex + 1, dp)
        sum2 = count_subsets_recursive(num, sum, currentIndex + 1, dp)
        dp[currentIndex][sum] = sum1 + sum2
    return dp[currentIndex][sum]


def main():
  print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
  print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
