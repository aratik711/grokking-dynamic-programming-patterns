"""

Given a set of positive numbers, partition the set into two subsets with a minimum difference between their subset sums.

Example 1:#
Input: {1, 2, 3, 9}
Output: 3
Explanation: We can partition the given set into two subsets where the minimum absolute difference
between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.
Example 2:#
Input: {1, 2, 7, 1, 5}
Output: 0
Explanation: We can partition the given set into two subsets where the minimum absolute difference
between the sum of numbers is '0'. Following are the two subsets: {1, 2, 5} & {7, 1}.
Example 3:#
Input: {1, 3, 100, 4}
Output: 92
Explanation: We can partition the given set into two subsets where the minimum absolute difference
between the sum of numbers is '92'. Here are the two subsets: {1, 3, 4} & {100}.

The time complexity of the above algorithm is exponential O(2^n), where ‘n’ represents the total number. The space complexity is O(n) which is used to store the recursion stack.

"""

def can_partition(num):
    return can_partition_recurse(num, 0, 0, 0)

def can_partition_recurse(num, currentIndex, sum1, sum2):
    if currentIndex == len(num):
        return abs(sum1 - sum2)
    diff1 = can_partition_recurse(num, currentIndex + 1, sum1 + num[currentIndex], sum2)
    diff2 = can_partition_recurse(num, currentIndex + 1, sum1, sum2 + num[currentIndex])
    return min(diff1, diff2)


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 9])))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
  print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()
