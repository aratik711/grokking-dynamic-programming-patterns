"""
Given a string, we want to cut it into pieces such that each piece is a palindrome. Write a function to return the minimum number of cuts needed.

Example 1:

Input: "abdbca"
Output: 3
Explanation: Palindrome pieces are "a", "bdb", "c", "a".
Example 2:

Input: = "cddpd"
Output: 2
Explanation: Palindrome pieces are "c", "d", "dpd".
Example 3:

Input: = "pqr"
Output: 2
Explanation: Palindrome pieces are "p", "q", "r".
Example 4:

Input: = "pp"
Output: 0
Explanation: We do not need to cut, as "pp" is a palindrome.



"""
def find_MPP_cuts(str):
    n = len(str)
    dp = [[-1 for x in range(n)]for y in range(n)]
    dpIsPallindrome = [[-1 for x in range(n)]for y in range(n)]
    return find_MPP_cuts_recurse(str, 0 , len(str) - 1, dp, dpIsPallindrome)

def find_MPP_cuts_recurse(str, start, end, dp, dpIsPallindrome):
    if start >= end or is_pallindrome(str, start, end, dpIsPallindrome):
        return 0
    if dp[start][end] == -1:
        minCuts = end - start
        for i in range(start, end+1):
            if is_pallindrome(str, start, i, dpIsPallindrome):
                minCuts = min(minCuts, 1+find_MPP_cuts_recurse(str, i+1, end, dp, dpIsPallindrome))
        dp[start][end] = minCuts
    return dp[start][end]


def is_pallindrome(str, start, end, dpIsPallindrome):
    if dpIsPallindrome[start][end] == -1:
        dpIsPallindrome[start][end] = 1
    i, j = start, end
    while(i < j):
        if str[i] != str[j]:
            dpIsPallindrome[start][end] = 0
            break
        i += 1
        j -= 1
        if i < j and dpIsPallindrome[i][j] != -1:
            dpIsPallindrome[start][end] = dpIsPallindrome[i][j]
            break
    return True if dpIsPallindrome[start][end] == 1 else False


def main():
  print(find_MPP_cuts("abdbca"))
  print(find_MPP_cuts("cdpdd"))
  print(find_MPP_cuts("pqr"))
  print(find_MPP_cuts("pp"))
  print(find_MPP_cuts("madam"))


main()
