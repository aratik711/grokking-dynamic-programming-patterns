"""

Given a string and a pattern, write a method to count the number of times the pattern appears in the string as a subsequence.

Example 1: Input: string: “baxmx”, pattern: “ax”
Output: 2
Explanation: {baxmx, baxmx}.

Example 2:

Input: string: “tomorrow”, pattern: “tor”
Output: 4
Explanation: Following are the four occurences: {tomorrow, tomorrow, tomorrow, tomorrow}.

The time complexity of the above algorithm is exponential O(2^{m})
, where ‘m’ is the length of the string, as our recursion stack will not be deeper than m. The space complexity is O(m)
 which is used to store the recursion stack.


"""
def find_SPM_count(str, pat):
    return find_SPM_count_recurse(str, pat, 0, 0)

def find_SPM_count_recurse(str, pat, strIndex, patIndex):
    if patIndex == len(pat):
        return 1
    if strIndex == len(str):
        return 0
    c1 = 0
    if str[strIndex] == pat[patIndex]:
        c1 = find_SPM_count_recurse(str, pat, strIndex + 1, patIndex + 1)
    c2 = find_SPM_count_recurse(str, pat, strIndex + 1, patIndex)
    return c1 + c2

def main():
  print(find_SPM_count("baxmx", "ax"))
  print(find_SPM_count("tomorrow", "tor"))


main()
