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

In each function call, we are either having one recursive call or two recursive calls (we will never have three recursive calls); hence, the time complexity of the above algorithm is exponential O(2^n)
, where ‘n’ is the length of the input sequence. The space complexity is O(n), which is used to store the recursion stack.



"""
def find_LPS_length(str):
    return find_LPS_length_recurse(str, 0, len(str) - 1)

def find_LPS_length_recurse(str, start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    if str[start] == str[end]:
        return 2 + find_LPS_length_recurse(str, start + 1, end - 1)
    c1 = find_LPS_length_recurse(str, start, end - 1)
    c2 = find_LPS_length_recurse(str, start + 1, end)
    return max(c1,c2)

def main():
  print(find_LPS_length("abdbca"))
  print(find_LPS_length("cddpd"))
  print(find_LPS_length("pqr"))


main()
