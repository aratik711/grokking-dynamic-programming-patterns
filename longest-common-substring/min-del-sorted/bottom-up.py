"""

Given a number sequence, find the minimum number of elements that should be deleted to make the remaining sequence sorted.

Example 1:

Input: {4,2,3,6,10,1,12}
Output: 2
Explanation: We need to delete {4,1} to make the remaing sequence sorted {2,3,6,10,12}.
Example 2:

Input: {-4,10,3,7,15}
Output: 1
Explanation: We need to delete {10} to make the remaing sequence sorted {-4,3,7,15}.
Example 3:

Input: {3,2,1,0}
Output: 3
Explanation: Since the elements are in reverse order, we have to delete all except one to get a
sorted sequence. Sorted sequences are {3}, {2}, {1}, and {0}

The time complexity of the above algorithm is O(n^2)
 and the space complexity is O(n).

"""
def find_minimum_deletions(nums):
    return len(nums) - find_LIS_length(nums)

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
                maxLength = max(dp[i], maxLength)
    return maxLength

def main():
  print(find_minimum_deletions([4, 2, 3, 6, 10, 1, 12]))
  print(find_minimum_deletions([-4, 10, 3, 7, 15]))
  print(find_minimum_deletions([3, 2, 1, 0]))


main()
