"""

Given a number array representing the wealth of n houses, determine the maximum amount of money the thief can steal without alerting the security system.

Example 1:

Input: {2, 5, 1, 3, 6, 2, 4}
Output: 15
Explanation: The thief should steal from houses 5 + 6 + 4
Example 2:

Input: {2, 10, 14, 8, 1}
Output: 18
Explanation: The thief should steal from houses 10 + 8

The only restriction the thief has is that he can’t steal from two consecutive houses, as that would alert the security system. How should the thief maximize his stealing?

The time complexity of the above algorithm is exponential O(2^n)
. The space complexity is O(n) which is used to store the recursion stack.

"""

def find_max_steal(wealth):
  return find_max_steal_recurse(wealth, 0)

def find_max_steal_recurse(wealth, currentIndex):
    if currentIndex >= len(wealth):
        return 0
    stealCurrent = wealth[currentIndex] + find_max_steal_recurse(wealth, currentIndex + 2)
    skipCurrent = find_max_steal_recurse(wealth, currentIndex + 1)
    return max(stealCurrent, skipCurrent)


def main():

  print(find_max_steal([2, 5, 1, 3, 6, 2, 4]))
  print(find_max_steal([2, 10, 14, 8, 1]))


main()
