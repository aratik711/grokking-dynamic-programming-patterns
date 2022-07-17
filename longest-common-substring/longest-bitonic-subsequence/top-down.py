"""

Given a number sequence, find the length of its Longest Bitonic Subsequence (LBS). A subsequence is considered bitonic if it is monotonically increasing and then monotonically decreasing.

Example 1:

Input: {4,2,3,6,10,1,12}
Output: 5
Explanation: The LBS is {2,3,6,10,1}.
Example 2:

Input: {4,2,5,9,7,6,10,3,1}
Output: 7
Explanation: The LBS is {4,5,9,7,6,3,1}.


"""
def find_LBS_length(nums):
    n = len(nums)
    lds = [[-1 for x in range(n+1)]for y in range(n)]
    ldsRev = [[-1 for x in range(n+1)]for y in range(n)]
    maxLength = 0
    for i in range(len(nums)):
        c1 = find_LDS_length(nums, i, -1, lds)
        c2 = find_LDS_length_rev(nums, i, -1, ldsRev)
        maxLength = max(maxLength, c1 + c2 - 1)
    return maxLength

def find_LDS_length(nums, currentIndex, previousIndex, dp):
    if currentIndex == len(nums):
        return 0
    if dp[currentIndex][previousIndex+1] == -1:
        # include nums[currentIndex] if it is smaller than the previous number
        c1 = 0
        if previousIndex == -1 or nums[currentIndex] < nums[previousIndex]:
            c1 = 1 + find_LDS_length(nums, currentIndex + 1, currentIndex, dp)
        c2 = find_LDS_length(nums, currentIndex + 1, previousIndex, dp)
        dp[currentIndex][previousIndex + 1] = max(c1, c2)
    return dp[currentIndex][previousIndex + 1]

def find_LDS_length_rev(nums, currentIndex, previousIndex, dp):
    if currentIndex < 0:
        return 0
    if dp[currentIndex][previousIndex+1] == -1:
        # include nums[currentIndex] if it is smaller than the previous number
        c1 = 0
        if previousIndex == -1 or nums[currentIndex] < nums[previousIndex]:
            c1 = 1 + find_LDS_length_rev(nums, currentIndex - 1, currentIndex, dp)
        c2 = find_LDS_length_rev(nums, currentIndex - 1, previousIndex, dp)
        dp[currentIndex][previousIndex + 1] = max(c1, c2)
    return dp[currentIndex][previousIndex + 1]


def main():
  print(find_LBS_length([4, 2, 3, 6, 10, 1, 12]))
  print(find_LBS_length([4, 2, 5, 9, 7, 6, 10, 3, 1]))


main()
