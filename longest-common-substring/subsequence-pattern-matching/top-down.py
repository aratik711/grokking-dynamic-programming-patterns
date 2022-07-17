"""

Given a string and a pattern, write a method to count the number of times the pattern appears in the string as a subsequence.

Example 1: Input: string: “baxmx”, pattern: “ax”
Output: 2
Explanation: {baxmx, baxmx}.

Example 2:

Input: string: “tomorrow”, pattern: “tor”
Output: 4
Explanation: Following are the four occurences: {tomorrow, tomorrow, tomorrow, tomorrow}.


"""
def find_SPM_count(str, pat):
    dp = [[-1 for x in range(len(pat))]for y in range(len(str))]
    return find_SPM_count_recurse(str, pat, 0, 0, dp)

def find_SPM_count_recurse(str, pat, strIndex, patIndex, dp):
    if patIndex == len(pat):
        return 1
    if strIndex == len(str):
        return 0
    if dp[strIndex][patIndex] == -1:
        c1 = 0
        if str[strIndex] == pat[patIndex]:
            c1 = find_SPM_count_recurse(str, pat, strIndex + 1, patIndex + 1, dp)
        c2 = find_SPM_count_recurse(str, pat, strIndex + 1, patIndex, dp)
        dp[strIndex][patIndex] = c1 + c2
    return dp[strIndex][patIndex]

def main():
  print(find_SPM_count("baxmx", "ax"))
  print(find_SPM_count("tomorrow", "tor"))


main()
