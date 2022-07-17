"""

Given two strings ‘s1’ and ‘s2’, find the length of the longest subsequence which is common in both the strings.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: s1 = "abdca"
       s2 = "cbda"
Output: 3
Explanation: The longest common subsequence is "bda".
Example 2:

Input: s1 = "passport"
       s2 = "ppsspt"
Output: 5
Explanation: The longest common subsequence is "psspt".


The time complexity of the above algorithm is exponential O(2^{m+n})
, where ‘m’ and ‘n’ are the lengths of the two input strings. The space complexity is O(n+m)
 which is used to store the recursion stack.



"""


def find_LCS_length(s1, s2):
    return find_LCS_length_recurse(s1, s2, 0, 0)

def find_LCS_length_recurse(s1, s2, i1, i2):
    if i1 == len(s1) or i2 == len(s2):
        return 0
    if s1[i1] == s2[i2]:
        return 1 + find_LCS_length_recurse(s1, s2, i1+1, i2+1)
    c1 = find_LCS_length_recurse(s1, s2, i1+1, i2)
    c2 = find_LCS_length_recurse(s1, s2, i1, i2+1)
    return max(c1, c2)

def main():
  print(find_LCS_length("abdca", "cbda"))
  print(find_LCS_length("passport", "ppsspt"))


main()
