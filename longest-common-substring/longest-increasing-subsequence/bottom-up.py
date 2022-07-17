"""

Given a number sequence, find the length of its Longest Increasing Subsequence (LIS). In an increasing subsequence, all the elements are in increasing order (from lowest to highest).

Example 1:

Input: {4,2,3,6,10,1,12}
Output: 5
Explanation: The LIS is {2,3,6,10,12}.
Example 1:

Input: {-4,10,3,7,15}
Output: 4
Explanation: The LIS is {-4,3,7,15}.

If the number at the current index is bigger than the number at the previous index, we increment the count for LIS up to the current index.
But if there is a bigger LIS without including the number at the current index, we take that.
So we need to find all the increasing subsequences for the number at index ‘i’, from all the previous numbers (i.e. number till index ‘i-1’), to eventually find the longest increasing subsequence.

If ‘i’ represents the ‘currentIndex’ and ‘j’ represents the ‘previousIndex’, our recursive formula would look like:

if num[i] > num[j] => dp[i] = dp[j] + 1 if there is no bigger LIS for 'i'

The time complexity of the above algorithm is O(n^2)
 and the space complexity is O(n)

"""
def find_LIS_length(nums):
    n = len(nums)
    dp = [0 for x in range(n)]
    dp[0] = 1
    maxLength = 1
    for i in range(1, n):
        dp[i] = 1
        for j in range(i):
            if nums[i] > nums[j] and dp[i] <= dp[j]:
                dp[i] = dp[j] + 1
                maxLength = max(maxLength, dp[i])
    return maxLength

def main():
  print(find_LIS_length([4, 2, 3, 6, 10, 1, 12]))
  print(find_LIS_length([-4, 10, 3, 7, 15]))


main()
