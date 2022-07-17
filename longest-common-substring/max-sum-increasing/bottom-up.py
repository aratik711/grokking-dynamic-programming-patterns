"""

Given a number sequence, find the increasing subsequence with the highest sum. Write a method that returns the highest sum.

Example 1:

Input: {4,1,2,6,10,1,12}
Output: 32
Explanation: The increaseing sequence is {4,6,10,12}.
Please note the difference, as the LIS is {1,2,6,10,12} which has a sum of '31'.
Example 2:

Input: {-4,10,3,7,15}
Output: 25
Explanation: The increaseing sequences are {10, 15} and {3,7,15}.

If the number at the current index is bigger than the number at the previous index, we include that number in the sum for an increasing sequence up to the current index.
But if there is a maximum sum increasing subsequence (MSIS), without including the number at the current index, we take that.
So we need to find all the increasing subsequences for a number at index i, from all the previous numbers (i.e. numbers till index i-1), to find MSIS.

If i represents the currentIndex and ‘j’ represents the previousIndex, our recursive formula would look like:

    if num[i] > num[j] => dp[i] = dp[j] + num[i] if there is no bigger MSIS for 'i'

The time complexity of the above algorithm is O(n^2)
 and the space complexity is O(n).

"""
def find_MSIS(nums):
    n = len(nums)
    dp = [0 for x in range(n)]
    dp[0] = nums[0]
    maxSum = dp[0]
    for i in range(1, n):
        dp[i] = nums[i]
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + nums[i]:
                dp[i] = dp[j] + nums[i]
        maxSum = max(dp[i], maxSum)
    return maxSum


def main():
  print(find_MSIS([4, 1, 2, 6, 10, 1, 12]))
  print(find_MSIS([-4, 10, 3, 7, 15]))


main()
