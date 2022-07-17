"""

Given strings s1 and s2, we need to transform s1 into s2 by deleting, inserting, or replacing characters. Write a function to calculate the count of the minimum number of edit operations.

Example 1:

Input: s1 = "bat"
       s2 = "but"
Output: 1
Explanation: We just need to replace 'a' with 'u' to transform s1 to s2.
Example 2:

Input: s1 = "abdca"
       s2 = "cbda"
Output: 2
Explanation: We can replace first 'a' with 'c' and delete second 'c'.
Example 3:

Input: s1 = "passpot"
       s2 = "ppsspqrt"
Output: 3
Explanation: Replace 'a' with 'p', 'o' with 'q', and insert 'r'.

Since our memoization array dp[s1.length()][s2.length()] stores the results for all the subproblems, we can conclude that we will not have more than m*n
 subproblems (where ‘m’ and ‘n’ are the lengths of the two input strings.). This means that our time complexity will be O(m*n)

The above algorithm will be using O(m*n)
 space for the memoization array. Other than that we will use O(m+n)
 space for the recursion call-stack. So the total space complexity will be O(m*n + (m+n))
, which is asymptotically equivalent to O(m*n)

"""
def find_min_operations(s1, s2):
    dp = [[-1 for x in range(len(s2)+1)]for y in range(len(s1)+1)]
    return find_min_operations_recurse(s1, s2, 0, 0, dp)

def find_min_operations_recurse(s1, s2, i1, i2, dp):
    n1, n2 = len(s1), len(s2)
    if dp[i1][i2] == -1:
        # if we have reached the end of s1, then we have to insert all the remaining characters of s2
        if i1 == n1:
            return n2 - i2
        elif i2 == n2:
            return n1 - i1
        elif s1[i1] == s2[i2]:
            dp[i1][i2] = find_min_operations_recurse(s1, s2, i1+1, i2+1, dp)
        else:
            # perform deletion
            c1 = 1 + find_min_operations_recurse(s1, s2, i1+1, i2, dp)
            # perform insertion
            c2 = 1 + find_min_operations_recurse(s1, s2, i1, i2+1, dp)
            # perform replacement
            c3 = 1 + find_min_operations_recurse(s1, s2, i1+1, i2+1, dp)
            dp[i1][i2] = min(c1, min(c2, c3))
    return dp[i1][i2]

def main():
  print(find_min_operations("bat", "but"))
  print(find_min_operations("abdca", "cbda"))
  print(find_min_operations("passpot", "ppsspqrt"))


main()
