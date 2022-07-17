"""

Given a number ‘n’, implement a method to count how many possible ways there are to express ‘n’ as the sum of 1, 3, or 4.

Example 1:

n : 4
Number of ways = 4
Explanation: Following are the four ways we can express 'n' : {1,1,1,1}, {1,3}, {3,1}, {4}
Example 2:

n : 5
Number of ways = 6
Explanation: Following are the six ways we can express 'n' : {1,1,1,1,1}, {1,1,3}, {1,3,1}, {3,1,1},
{1,4}, {4,1}

The time complexity of the above algorithm is exponential O(3^n)
. The space complexity is O(n) which is used to store the recursion stack.



"""
def count_ways(n):
    if n <= 2:
        return 1
    if n == 3:
        return 2
    count1 = count_ways(n-1)
    count2 = count_ways(n-3)
    count3 = count_ways(n-4)
    return count1 + count2 + count3


def main():

  print(count_ways(4))
  print(count_ways(5))
  print(count_ways(6))


main()
