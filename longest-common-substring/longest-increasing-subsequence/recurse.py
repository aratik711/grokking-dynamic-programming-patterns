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

The time complexity of the above algorithm is exponential O(2^n)
, where ‘n’ is the lengths of the input array. The space complexity is O(n)
 which is used to store the recursion stack.



"""
def find_LIS_length(nums):
    return find_LIS_length_recurse(nums, 0 , -1)

def find_LIS_length_recurse(nums, currentIndex, previousIndex):
    if currentIndex == len(nums):
        return 0
    c1 = 0
    if previousIndex == -1 or nums[currentIndex] > nums[previousIndex]:
        c1 = 1 + find_LIS_length_recurse(nums, currentIndex + 1, currentIndex)
    c2 = find_LIS_length_recurse(nums, currentIndex + 1, previousIndex)
    return max(c1,c2)

def main():
  print(find_LIS_length([4, 2, 3, 6, 10, 1, 12]))
  print(find_LIS_length([-4, 10, 3, 7, 15]))


main()
