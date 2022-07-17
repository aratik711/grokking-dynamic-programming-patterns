"""

Given an array of positive numbers, where each element represents the max number of jumps that can be made forward from that element, write a program to find the minimum number of jumps needed to reach the end of the array (starting from the first element). If an element is 0, then we cannot move through that element.

Example 1:

Input = {2,1,1,1,4}
Output = 3
Explanation: Starting from index '0', we can reach the last index through: 0->2->3->4
Example 2:

Input = {1,1,3,6,9,3,0,1,3}
Output = 4
Explanation: Starting from index '0', we can reach the last index through: 0->1->2->3->8


The time complexity of the above algorithm is O(2^n)
, where ‘n’ is the size of the input array. The ‘while loop’ can execute a maximum of ‘n’ times (for the case where we can jump to all the steps ahead) and since in each iteration, the function recursively calls itself, therefore, the time complexity is O(2^n)
. The space complexity is O(n) which is used to store the recursion stack.



"""
import math


def count_min_jumps(jumps):
  return count_min_jumps_recurse(jumps, 0)

def count_min_jumps_recurse(jumps, currentIndex):
    n = len(jumps)
    if jumps[currentIndex] == 0:
        return math.inf
    if currentIndex == n-1:
        return 0
    totalJumps = math.inf
    start, end = currentIndex + 1, currentIndex + jumps[currentIndex]
    while start < n and start <= end:
        minJumps = count_min_jumps_recurse(jumps, start)
        start += 1
        if minJumps != math.inf:
            totalJumps = min(totalJumps, minJumps + 1)
    return totalJumps

def main():

  print(count_min_jumps([2, 1, 1, 1, 4]))
  print(count_min_jumps([1, 1, 3, 6, 9, 3, 0, 1, 3]))


main()
