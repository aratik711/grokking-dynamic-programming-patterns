"""

Given a string, find the length of its Longest Palindromic Substring (LPS). In a palindromic string, elements read the same backward and forward.

Example 1:

Input: "abdbca"
Output: 3
Explanation: LPS is "bdb".
Example 2:

Input: = "cddpd"
Output: 3
Explanation: LPS is "dpd".
Example 3:

Input: = "pqr"
Output: 1
Explanation: LPS could be "p", "q" or "r".


The above algorithm has a time and space complexity of O(n^2)
 because we will not have more than n*n subproblems.


"""
def find_LPS_length(str):
    n = len(str)
    dp = [[-1 for x in range(n)] for y in range(n)]
    return find_LPS_length_recurse(str, 0, len(str) - 1, dp)

def find_LPS_length_recurse(str, start, end, dp):
    if start > end:
        return 0
    if start == end:
        return 1
    if dp[start][end] == -1:
        if str[start] == str[end]:
            remainingLength = end - start - 1
            if remainingLength == find_LPS_length_recurse(str, start + 1, end - 1, dp):
                dp[start][end] = remainingLength + 2
                return dp[start][end]
        c1 = find_LPS_length_recurse(str, start + 1, end, dp)
        c2 = find_LPS_length_recurse(str, start, end - 1, dp)
        dp[start][end] = max(c1, c2)
    return dp[start][end]

def main():
  print(find_LPS_length("abdbca"))
  print(find_LPS_length("cddpd"))
  print(find_LPS_length("pqr"))


main()
