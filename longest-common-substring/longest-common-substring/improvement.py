"""

Given two strings ‘s1’ and ‘s2’, find the length of the longest substring which is common in both the strings.

Example 1:

Input: s1 = "abdca"
       s2 = "cbda"
Output: 2
Explanation: The longest common substring is "bd".
Example 2:

Input: s1 = "passport"
       s2 = "ppsspt"
Output: 3
Explanation: The longest common substring is "ssp".

The time and space complexity of the above algorithm is O(m*n)
, where ‘m’ and ‘n’ are the lengths of the two input strings.

"""


def find_LCS_length(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[0 for x in range(n2+1)]for y in range(2)]
    maxLength = 0
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            dp[i%2][j] = 0
            if s1[i-1] == s2[j-1]:
                dp[i%2][j] = 1 + dp[(i-1)%2][j-1]
                maxLength = max(maxLength, dp[i%2][j])
    return maxLength

def main():
  print(find_LCS_length("abdca", "cbda"))
  print(find_LCS_length("passport", "ppsspt"))


main()
