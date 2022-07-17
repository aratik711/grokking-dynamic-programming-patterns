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


Due to the three recursive calls, the time complexity of the above algorithm is exponential O(3^n)
, where ‘n’ is the length of the input string. The space complexity is O(n)
 which is used to store the recursion stack.



"""
def find_LPS_length(str):
    return find_LPS_length_recurse(str, 0, len(str) - 1)

def find_LPS_length_recurse(str, start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    if str[start] == str[end]:
        remainingLength = end - start - 1
        if remainingLength == find_LPS_length_recurse(str, start + 1, end - 1):
            return remainingLength + 2
    c1 = find_LPS_length_recurse(str, start + 1, end)
    c2 = find_LPS_length_recurse(str, start, end - 1)
    return max(c1, c2)

def main():
  print(find_LPS_length("abdbca"))
  print(find_LPS_length("cddpd"))
  print(find_LPS_length("pqr"))


main()
