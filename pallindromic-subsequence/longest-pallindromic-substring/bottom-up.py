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


The time and space complexity of the above algorithm is O(n^2)
, where ‘n’ is the length of the input string.

https://en.wikipedia.org/wiki/Longest_palindromic_substring

"""
def find_LPS_length(str):
    n = len(str)
    dp = [[False for x in range(n)] for y in range(n)]
    for i in range(n):
        dp[i][i] = True
    maxLength = 1
    for start in range(n-1, -1, -1):
        for end in range(start+1, n):
            if str[start] == str[end]:
                if end - start == 1 or dp[start+1][end-1]:
                    dp[start][end] = True
                    maxLength = max(maxLength, end - start + 1)
    return maxLength

def main():
  print(find_LPS_length("abdbca"))
  print(find_LPS_length("cddpd"))
  print(find_LPS_length("pqr"))


main()
