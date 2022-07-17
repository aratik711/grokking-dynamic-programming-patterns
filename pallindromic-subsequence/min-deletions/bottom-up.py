"""

Given a string, find the minimum number of characters that we can remove to make it a palindrome.

Example 1:

Input: "abdbca"
Output: 1
Explanation: By removing "c", we get a palindrome "abdba".
Example 2:

Input: = "cddpd"
Output: 2
Explanation: Deleting "cp", we get a palindrome "ddd".
Example 3:

Input: = "pqr"
Output: 2
Explanation: We have to remove any two characters to get a palindrome, e.g. if we
remove "pq", we get palindrome "r".

The time and space complexity of the above algorithm is O(n^2)
, where ‘n’ is the length of the input string.

"""
def find_minimum_deletions(str):
    # subtracting the length of Longest Palindromic Subsequence from the length of
    # the input string to get minimum number of deletions
    return len(str) - find_LPS_length(str)


def find_LPS_length(str):
    n = len(str)
    dp = [[0 for x in range(n)]for y in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for start in range(n - 1, -1, -1):
        for end in range(start + 1, n):
            if str[start] == str[end]:
                dp[start][end] = 2 + dp[start+1][end-1]
            else:
                dp[start][end] = max(dp[start + 1][end], dp[start][end-1])
    return dp[0][n-1]

def main():
  print(find_minimum_deletions("abdbca"))
  print(find_minimum_deletions("cddpd"))
  print(find_minimum_deletions("pqr"))


main()
