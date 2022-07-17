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

The time complexity of the above algorithm is O(n^2)
 and the space complexity is O(n)

"""
def find_LBS_length(nums):
    n = len(nums)
    lds = [0 for y in range(n)]
    ldsRev = [0 for y in range(n)]
    for i in range(n):
        lds[i] = 1
        for j in range(i-1, -1, -1):
            if nums[j] < nums[i]:
                lds[i] = max(lds[i], lds[j] + 1)
    for i in range(n-1, -1, -1):
        ldsRev[i] = 1
        for j in range(i+1, n):
            if nums[j] < nums[i]:
                ldsRev[i] = max(ldsRev[i], ldsRev[j] + 1)
    maxLength = 0
    for i in range(n):
        maxLength = max(maxLength, lds[i] + ldsRev[i] - 1)
    return maxLength


def main():
  print(find_LBS_length([4, 2, 3, 6, 10, 1, 12]))
  print(find_LBS_length([4, 2, 5, 9, 7, 6, 10, 3, 1]))


main()
