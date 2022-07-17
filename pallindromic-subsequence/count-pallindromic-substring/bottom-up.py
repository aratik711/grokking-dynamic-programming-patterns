"""

Given a string, find the total number of palindromic substrings in it. Please note we need to find the total number of substrings and not subsequences.

Example 1:

Input: "abdbca"
Output: 7
Explanation: Here are the palindromic substrings, "a", "b", "d", "b", "c", "a", "bdb".
Example 2:

Input: = "cddpd"
Output: 7
Explanation: Here are the palindromic substrings, "c", "d", "d", "p", "d", "dd", "dpd".
Example 3:

Input: = "pqr"
Output: 3
Explanation: Here are the palindromic substrings,"p", "q", "r".

The time and space complexity of the above algorithm is O(n^2)
, where ‘n’ is the length of the input string.



"""
def count_PS(str):
    n = len(str)
    # dp[i][j] will be 'true' if the string from index 'i' to index 'j' is a palindrome
    dp = [[False for x in range(n)]for y in range(n)]
    count = 0
    for i in range(n):
        dp[i][i] = True
        count += 1
    for start in range(n-1, -1, -1):
        for end in range(start + 1, n):
            if str[start] == str[end]:
                if end - start == 1 or dp[start+1][end-1]:
                    dp[start][end] = True
                    count += 1
    return count

def main():
  print(count_PS("abdbca"))
  print(count_PS("cddpd"))
  print(count_PS("pqr"))
  print(count_PS("qqq"))


main()
