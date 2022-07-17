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

Since our memoization array dp[nums.length()][nums.length()] stores the results for all the subproblems, we can conclude that we will not have more than N*N
 subproblems (where ‘N’ is the length of the input sequence). This means that our time complexity will be O(N^2)
The above algorithm will be using O(N^2)
 space for the memoization array. Other than that we will use O(N)
 space for the recursion call-stack. So the total space complexity will be O(N^2 + N)
, which is asymptotically equivalent to O(N^2)

"""
def find_LIS_length(nums):
    n = len(nums)
    dp = [[-1 for x in range(n+1)] for y in range(n)]
    return find_LIS_length_recurse(nums, 0 , -1, dp)

def find_LIS_length_recurse(nums, currentIndex, previousIndex, dp):
    if currentIndex == len(nums):
        return 0
    if dp[currentIndex][previousIndex] == -1:
        c1 = 0
        if previousIndex == -1 or nums[currentIndex] > nums[previousIndex]:
           c1 = 1 + find_LIS_length_recurse(nums, currentIndex + 1, currentIndex, dp)
        c2 = find_LIS_length_recurse(nums, currentIndex + 1, previousIndex, dp)
        dp[currentIndex][previousIndex] = max(c1,c2)
    return dp[currentIndex][previousIndex]

def main():
  print(find_LIS_length([4, 2, 3, 6, 10, 1, 12]))
  print(find_LIS_length([-4, 10, 3, 7, 15]))


main()
