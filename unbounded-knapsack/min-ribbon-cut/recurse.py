"""

We are given a ribbon of length ‘n’ and a set of possible ribbon lengths. We need to cut the ribbon into the maximum number of pieces that comply with the above-mentioned possible lengths. Write a method that will return the count of pieces.

Example 1:

n: 5
Ribbon Lengths: {2,3,5}
Output: 2
Explanation: Ribbon pieces will be {2,3}.
Example 2:

n: 7
Ribbon Lengths: {2,3}
Output: 3
Explanation: Ribbon pieces will be {2,2,3}.
Example 3:

n: 13
Ribbon Lengths: {3,5,7}
Output: 3
Explanation: Ribbon pieces will be {3,3,7}.

The above algorithm’s time complexity is exponential O(2^{L+N}), where ‘L’ represents total ribbon lengths, and ‘N’ is the total length that we want to cut. The space complexity will be O(L+N)



"""

import math


def count_ribbon_pieces(ribbonLengths, total):
    maxPieces = count_ribbon_pieces_recurse(ribbonLengths, total, 0)
    return -1 if maxPieces == -math.inf else maxPieces

def count_ribbon_pieces_recurse(ribbonLengths, total, currentIndex):
    if total == 0:
        return 0
    n = len(ribbonLengths)
    if n == 0 or currentIndex >= n:
        return -math.inf
    count1 = -math.inf
    if ribbonLengths[currentIndex] <= total:
        res = count_ribbon_pieces_recurse(ribbonLengths, total - ribbonLengths[currentIndex], currentIndex)
        if res != -math.inf:
            count1 = res + 1
    count2 = count_ribbon_pieces_recurse(ribbonLengths, total, currentIndex + 1)
    return max(count1, count2)

def main():
  print(count_ribbon_pieces([2, 3, 5], 5))
  print(count_ribbon_pieces([2, 3], 7))
  print(count_ribbon_pieces([3, 5, 7], 13))
  print(count_ribbon_pieces([3, 5], 7))


main()
