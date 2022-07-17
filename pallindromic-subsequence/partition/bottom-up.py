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

The time and space complexity of the above algorithm is O(n^2)
, where ‘n’ is the length of the input string.

"""
def find_MPP_cuts(str):
    n = len(str)
    # isPalindrome[i][j] will be 'true' if the string from index 'i' to index 'j' is a palindrome
    isPalindrome = [[False for x in range(n)]for y in range(n)]
    for i in range(n):
        isPalindrome[i][i] = True
    for start in range(n-1, -1, -1):
        for end in range(start+1, n):
            if str[start]== str[end]:
                if end - start == 1 or isPalindrome[start+1][end-1]:
                    isPalindrome[start][end] = True
    # now lets populate the second table, every index in 'cuts' stores the minimum cuts needed
    # for the substring from that index till the end
    cuts = [0 for x in range(n)]
    for start in range(n-1, -1, -1):
        minCuts = n
        for end in range(n-1, start-1, -1):
            if isPalindrome[start][end]:
                # we can cut here as we got a palindrome
                # also we don't need any cut if the whole substring is a palindrome
                minCuts = 0 if end == n-1 else min(minCuts, 1+cuts[end+1])
        cuts[start] = minCuts
    return cuts[0]



def main():
  print(find_MPP_cuts("abdbca"))
  print(find_MPP_cuts("cdpdd"))
  print(find_MPP_cuts("pqr"))
  print(find_MPP_cuts("pp"))
  print(find_MPP_cuts("madam"))


main()
