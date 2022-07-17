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

The above solution has a time complexity of O(n) and a constant space complexity O(1).

"""

def find_max_steal(wealth):
    n = len(wealth)
    if n == 0:
        return 0
    n1, n2 = 0, wealth[0]
    for i in range(1, n):
        n1, n2 = n2, max(n1 + wealth[i], n2)

    return n2


def main():

  print(find_max_steal([2, 5, 1, 3, 6, 2, 4]))
  print(find_max_steal([2, 10, 14, 8, 1]))


main()
