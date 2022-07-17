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

The time complexity of the above algorithm is exponential O(2^n), where ‘n’ represents the total number. The space complexity is O(n), this memory which will be used to store the recursion stack.

"""

def can_partition(num):
    s = sum(num)
    if s%2 != 0:
        return False
    return can_partition_recurse(num, s/2, 0)

def can_partition_recurse(num, sum, currentIndex):
    n = len(num)
    print(currentIndex, num, sum)
    if sum == 0:
        return True

    if n == 0 or currentIndex >= n:
        return False
    if num[currentIndex] <= sum:
        if(can_partition_recurse(num, sum - num[currentIndex], currentIndex + 1)):
            return True
    return can_partition_recurse(num, sum, currentIndex + 1)


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
