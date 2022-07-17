"""

Given three strings ‘m’, ‘n’, and ‘p’, write a method to find out if ‘p’ has been formed by interleaving ‘m’ and ‘n’. ‘p’ would be considered interleaving ‘m’ and ‘n’ if it contains all the letters from ‘m’ and ‘n’ and the order of letters is preserved too.

Example 1:

Input: m="abd", n="cef", p="abcdef"
Output: true
Explanation: 'p' contains all the letters from 'm' and 'n' and preserves their order too.
Example 2:

Input: m="abd", n="cef", p="adcbef"
Output: false
Explanation: 'p' contains all the letters from 'm' and 'n' but does not preserve the order.
Example 3:

Input: m="abc", n="def", p="abdccf"
Output: false
Explanation: 'p' does not contain all the letters from 'm' and 'n'.
Example 4:

Input: m="abcdef", n="mnop", p="mnaobcdepf"
Output: true
Explanation: 'p' contains all the letters from 'm' and 'n' and preserves their order too.

If the character m[mIndex] matches the character p[pIndex], we will take the matching result up to mIndex-1 and nIndex.
If the character n[nIndex] matches the character p[pIndex], we will take the matching result up to mIndex and nIndex-1.

The time and space complexity of the above algorithm is O(m*n)
, where ‘m’ and ‘n’ are the lengths of the two interleaving strings.

"""
def find_SI(m, n,  p):
    mLen, nLen, pLen = len(m), len(n), len(p)
    dp = [[False for x in range(nLen+1)] for y in range(mLen+1)]
    if mLen + nLen != pLen:
        return False
    for mIndex in range(mLen+1):
        for nIndex in range(nLen+1):
            if mIndex == 0 and nIndex == 0:
                dp[mIndex][nIndex] = True
            # if 'm' is empty, we need to check the interleaving with 'n' only
            elif mIndex == 0 and n[nIndex-1] == p[mIndex+nIndex-1]:
                dp[mIndex][nIndex] = dp[mIndex][nIndex-1]
            elif nIndex == 0 and m[mIndex-1] == p[mIndex+nIndex-1]:
                dp[mIndex][nIndex] = dp[mIndex-1][nIndex]
            else:
                # if the letter of 'm' and 'p' match, we take whatever is matched till mIndex-1
                if mIndex > 0 and m[mIndex-1] == p[mIndex+nIndex-1]:
                    dp[mIndex][nIndex] = dp[mIndex-1][nIndex]
                # if the letter of 'n' and 'p' match, we take whatever is matched till nIndex-1 too
                # note the '|=', this is required when we have common letters
                if nIndex > 0 and n[nIndex-1] == p[mIndex+nIndex-1]:
                    dp[mIndex][nIndex] |= dp[mIndex][nIndex-1]
    return dp[mLen][nLen]


def main():
  print(find_SI("abd", "cef", "abcdef"))
  print(find_SI("abd", "cef", "adcbef"))
  print(find_SI("abc", "def", "abdccf"))
  print(find_SI("abcdef", "mnop", "mnaobcdepf"))


main()
