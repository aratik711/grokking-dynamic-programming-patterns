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


The time complexity of the above algorithm is exponential O(2^{m+n})
, where ‘m’ and ‘n’ are the lengths of the two interleaving strings. The space complexity is O(m+n)
, the value that is used to store the recursion stack.


"""
def find_SI(m, n,  p):
    return find_SI_recurse(m, n, p, 0, 0, 0)

def find_SI_recurse(m, n, p, mIndex, nIndex, pIndex):
    mLen, nLen, pLen = len(m), len(n), len(p)
    if mIndex == mLen and nIndex == nLen and pIndex == pLen:
        return True
    if pIndex == pLen:
        return False
    b1, b2 = False, False
    if mIndex < mLen and m[mIndex] == p[pIndex]:
        b1 = find_SI_recurse(m, n, p, mIndex+1, nIndex, pIndex+1)
    if nIndex < nLen and n[nIndex] == p[pIndex]:
        b2 = find_SI_recurse(m, n, p, mIndex, nIndex+1, pIndex+1)
    return b1 or b2



def main():
  print(find_SI("abd", "cef", "abcdef"))
  print(find_SI("abd", "cef", "adcbef"))
  print(find_SI("abc", "def", "abdccf"))
  print(find_SI("abcdef", "mnop", "mnaobcdepf"))


main()
