"""

Given a string and a pattern, write a method to count the number of times the pattern appears in the string as a subsequence.

Example 1: Input: string: “baxmx”, pattern: “ax”
Output: 2
Explanation: {baxmx, baxmx}.

Example 2:

Input: string: “tomorrow”, pattern: “tor”
Output: 4
Explanation: Following are the four occurences: {tomorrow, tomorrow, tomorrow, tomorrow}.

If the character at the strIndex (in the string) matches the character at patIndex (in the pattern), the count of the SPM would be equal to the count of SPM up to strIndex-1 and patIndex-1.
At every step, we can always skip a character from the string to try matching the remaining string with the pattern; therefore, we can add the SPM count from the indexes strIndex-1 and patIndex.

The time and space complexity of the above algorithm is O(m*n)
, where ‘m’ and ‘n’ are the lengths of the string and the pattern respectively.

"""
def find_SPM_count(str, pat):
    strLen, patLen = len(str), len(pat)
    if patLen == 0:
        return 1
    if strLen == 0 or patLen > strLen:
        return 0
    dp = [[0 for x in range(patLen + 1)]for y in range(strLen + 1)]
    for i in range(strLen + 1):
        dp[i][0] = 1
    for strIndex in range(1, strLen+1):
        for patIndex in range(1, patLen + 1):
            if str[strIndex-1] == pat[patIndex-1]:
                dp[strIndex][patIndex] = dp[strIndex-1][patIndex-1]
            dp[strIndex][patIndex] += dp[strIndex-1][patIndex]
    return dp[strLen][patLen]

def main():
  print(find_SPM_count("baxmx", "ax"))
  print(find_SPM_count("tomorrow", "tor"))


main()
