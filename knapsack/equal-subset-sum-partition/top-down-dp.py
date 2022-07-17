"""

Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both the subsets is equal.

Example 1: #
Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}
Example 2: #
Input: {1, 1, 3, 4, 7}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 3, 4} & {1, 7}
Example 3: #
Input: {2, 3, 4, 6}
Output: False
Explanation: The given set cannot be partitioned into two subsets with equal sum.

The above algorithm has time and space complexity of O(N*S), where ‘N’ represents total numbers and ‘S’ is the total sum of all the numbers.

"""

def can_partition(num):
    s = sum(num)
    if s%2 != 0:
        return False
    dp = [ [ -1 for x in range(int(s/2)+1)] for y in range(len(num))]
    print(dp)
    return True if can_partition_recurse(num, int(s/2), 0, dp) == 1 else False

def can_partition_recurse(num, sum, currentIndex, dp):
    n = len(num)
    print(currentIndex, num, sum)
    if sum == 0:
        return True

    if n == 0 or currentIndex >= n:
        return False
    if dp[currentIndex][sum] == -1:
        if num[currentIndex] <= sum:
            if(can_partition_recurse(num, sum - num[currentIndex], currentIndex + 1, dp)):
                dp[currentIndex][sum] = 1
                return 1
    dp[currentIndex][sum] = can_partition_recurse(num, sum, currentIndex + 1, dp)
    return dp[currentIndex][sum]


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
