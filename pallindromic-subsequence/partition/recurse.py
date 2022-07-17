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

The time complexity of the above algorithm is exponential O(2^n)
, where ‘n’ is the length of the input string. The space complexity is O(n)

 which is used to store the recursion stack.



"""
def find_MPP_cuts(str):
    return find_MPP_cuts_recurse(str, 0 , len(str) - 1)

def find_MPP_cuts_recurse(str, start, end):
    if start >= end or is_pallindrome(str, start, end):
        return 0
    minCuts = end - start
    for i in range(start, end+1):
        if is_pallindrome(str, start, i):
            minCuts = min(minCuts, 1+find_MPP_cuts_recurse(str, i+1, end))
    return minCuts


def is_pallindrome(str, start, end):
    while(start < end):
        if str[start] != str[end]:
            return False
        start += 1
        end -= 1
    return True


def main():
  print(find_MPP_cuts("abdbca"))
  print(find_MPP_cuts("cdpdd"))
  print(find_MPP_cuts("pqr"))
  print(find_MPP_cuts("pp"))
  print(find_MPP_cuts("madam"))


main()
