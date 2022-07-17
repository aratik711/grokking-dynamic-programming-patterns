"""

Given a sequence, find the length of its Longest Palindromic Subsequence (LPS). In a palindromic subsequence, elements read the same backward and forward.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: "abdbca"
Output: 5
Explanation: LPS is "abdba".
Example 2:

Input: = "cddpd"
Output: 3
Explanation: LPS is "ddd".
Example 3:

Input: = "pqr"
Output: 1
Explanation: LPS could be "p", "q" or "r".

The time and space complexity of the above algorithm is O(n^2)
, where ‘n’ is the length of the input sequence.


"""
def find_LPS_length(str):
    n = len(str)
    # dp[i][j] stores the length of LPS from index 'i' to index 'j'
    dp = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        dp[i][i] = 1

    for start in range(n-1, -1, -1):
        for end in range(start + 1, n):
            # case 1: elements at the beginning and the end are the same
            if str[start] == str[end]:
                dp[start][end] = 2 + dp[start+1][end-1]
            else:
                dp[start][end] = max(dp[start+1][end], dp[start][end-1])
    return dp[0][n-1]

def main():
  print(find_LPS_length("abdbca"))
  print(find_LPS_length("cddpd"))
  print(find_LPS_length("pqr"))


main()
