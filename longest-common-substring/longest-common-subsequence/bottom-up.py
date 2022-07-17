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

The time and space complexity of the above algorithm is O(m*n)
, where ‘m’ and ‘n’ are the lengths of the two input strings.

"""


def find_LCS_length(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[0 for x in range(n2+1)]for y in range(n1+1)]
    maxLength = 0
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[i][j]

def main():
  print(find_LCS_length("abdca", "cbda"))
  print(find_LCS_length("passport", "ppsspt"))


main()
