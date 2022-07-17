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



"""
def find_SI(m, n,  p):
    return find_SI_recurse(m, n, p, 0, 0, 0, {})

def find_SI_recurse(m, n, p, mIndex, nIndex, pIndex, dp):
    mLen, nLen, pLen = len(m), len(n), len(p)
    if mIndex == mLen and nIndex == nLen and pIndex == pLen:
        return True
    if pIndex == pLen:
        return False
    subProblemKey = str(mIndex) + "-" + str(nIndex) + "-" + str(pIndex)
    if subProblemKey not in dp:
        b1, b2 = False, False
        if mIndex < mLen and m[mIndex] == p[pIndex]:
            b1 = find_SI_recurse(m, n, p, mIndex+1, nIndex, pIndex+1, dp)
        if nIndex < nLen and n[nIndex] == p[pIndex]:
            b2 = find_SI_recurse(m, n, p, mIndex, nIndex+1, pIndex+1, dp)
        dp[subProblemKey] = b1 or b2
    return dp.get(subProblemKey)



def main():
  print(find_SI("abd", "cef", "abcdef"))
  print(find_SI("abd", "cef", "adcbef"))
  print(find_SI("abc", "def", "abdccf"))
  print(find_SI("abcdef", "mnop", "mnaobcdepf"))


main()
