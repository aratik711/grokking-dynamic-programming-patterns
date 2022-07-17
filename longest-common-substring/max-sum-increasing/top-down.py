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



"""
def find_MSIS(nums):
    dp = {}
    return find_MSIS_recurse(nums, 0, -1, 0, dp)

def find_MSIS_recurse(nums, currentIndex, previousIndex, sum, dp):
    if currentIndex == len(nums):
        return sum
    subProblemKey = str(currentIndex) + "-" + str(previousIndex) + "-" + str(sum)
    if subProblemKey not in dp:
        s1 = sum
        if previousIndex == -1 or nums[currentIndex] > nums[previousIndex]:
            s1 = find_MSIS_recurse(nums, currentIndex + 1, currentIndex, sum + nums[currentIndex], dp)
        s2 = find_MSIS_recurse(nums, currentIndex+1, previousIndex, sum, dp)
        dp[subProblemKey] = max(s1, s2)
    return dp.get(subProblemKey)

def main():
  print(find_MSIS([4, 1, 2, 6, 10, 1, 12]))
  print(find_MSIS([-4, 10, 3, 7, 15]))


main()
