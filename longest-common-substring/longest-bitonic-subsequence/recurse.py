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


The time complexity of the above algorithm is exponential O(2^n)
, where ‘n’ is the lengths of the input array. The space complexity is O(n)
 which is used to store the recursion stack.


"""
def find_LBS_length(nums):
    maxLength = 0
    for i in range(len(nums)):
        c1 = find_LDS_length(nums, i, -1)
        c2 = find_LDS_length_rev(nums, i, -1)
        maxLength = max(maxLength, c1 + c2 - 1)
    return maxLength

def find_LDS_length(nums, currentIndex, previousIndex):
    if currentIndex == len(nums):
        return 0
    c1 = 0
    if previousIndex == -1 or nums[currentIndex] < nums[previousIndex]:
        c1 = 1 + find_LDS_length(nums, currentIndex + 1, currentIndex)
    c2 = find_LDS_length(nums, currentIndex + 1, previousIndex)
    return max(c1, c2)

def find_LDS_length_rev(nums, currentIndex, previousIndex):
    if currentIndex < 0:
        return 0
    c1 = 0
    if previousIndex == -1 or nums[currentIndex] < nums[previousIndex]:
        c1 = 1 + find_LDS_length_rev(nums, currentIndex - 1, currentIndex)
    c2 = find_LDS_length_rev(nums, currentIndex - 1, previousIndex)
    return max(c1, c2)


def main():
  print(find_LBS_length([4, 2, 3, 6, 10, 1, 12]))
  print(find_LBS_length([4, 2, 5, 9, 7, 6, 10, 3, 1]))


main()
