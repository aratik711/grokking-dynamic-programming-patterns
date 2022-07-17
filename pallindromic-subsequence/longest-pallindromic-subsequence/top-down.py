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

This means that our time complexity will be O(N^2)
The above algorithm will be using O(N^2) space for the memoization array. Other than that we will use O(N)
 space for the recursion call-stack. So the total space complexity will be O(N^2 + N), which is asymptotically equivalent to O(N^2)



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
            dp[start][end] = 2 + find_LPS_length_recurse(str, start + 1, end - 1, dp)
        else:
            c1 = find_LPS_length_recurse(str, start, end - 1, dp)
            c2 = find_LPS_length_recurse(str, start + 1, end, dp)
            dp[start][end] = max(c1,c2)
    return dp[start][end]

def main():
  print(find_LPS_length("abdbca"))
  print(find_LPS_length("cddpd"))
  print(find_LPS_length("pqr"))


main()
