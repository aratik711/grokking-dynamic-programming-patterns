"""

A three element sequence (a1, a2, a3) will be an alternating sequence if its elements hold one of the following conditions:

{a1 > a2 < a3 } or { a1 < a2 > a3}.
Example 1:

Input: {1,2,3,4}
Output: 2
Explanation: There are many LAS: {1,2}, {3,4}, {1,3}, {1,4}
Example 2:

Input: {3,2,1,4}
Output: 3
Explanation: The LAS are {3,2,4} and {2,1,4}.
Example 3:

Input: {1,3,2,4}
Output: 4
Explanation: The LAS is {1,3,2,4}.



"""
def find_LAS_length(nums):
    n = len(nums)
    dp = [[[-1 for x in range(2)] for y in range(n)] for z in range(n)]
    # we have to start with two recursive calls, one where we will consider that the first element is
    # bigger than the second element and one where the first element is smaller than the second element
    return max(find_LAS_length_recurse(nums, -1, 0, True, dp), find_LAS_length_recurse(nums, -1, 0, False, dp))

def find_LAS_length_recurse(nums, previousIndex, currentIndex, isAsc, dp):
    if currentIndex == len(nums):
        return 0
    if dp[previousIndex+1][currentIndex][1 if isAsc else 0] == -1:
        c1 = 0
        if isAsc:
            if previousIndex == -1 or nums[previousIndex] < nums[currentIndex]:
                c1 = 1 + find_LAS_length_recurse(nums, currentIndex, currentIndex + 1, not isAsc, dp)
        else:
            if previousIndex == -1 or nums[previousIndex] > nums[currentIndex]:
                c1 = 1 + find_LAS_length_recurse(nums, currentIndex, currentIndex + 1, not isAsc, dp)
        c2 = find_LAS_length_recurse(nums, previousIndex, currentIndex + 1, isAsc, dp)
        dp[previousIndex+1][currentIndex][1 if isAsc else 0] = max(c1, c2)
    return dp[previousIndex+1][currentIndex][1 if isAsc else 0]

def main():
  print(find_LAS_length([1, 2, 3, 4]))
  print(find_LAS_length([3, 2, 1, 4]))
  print(find_LAS_length([1, 3, 2, 4]))


main()
