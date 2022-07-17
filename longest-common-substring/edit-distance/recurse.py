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

Because of the three recursive calls, the time complexity of the above algorithm is exponential O(3^{m+n})
, where ‘m’ and ‘n’ are the lengths of the two input strings. The space complexity is O(n+m)
 which is used to store the recursion stack.

"""
def find_min_operations(s1, s2):
    return find_min_operations_recurse(s1, s2, 0, 0)

def find_min_operations_recurse(s1, s2, i1, i2):
    n1, n2 = len(s1), len(s2)
    # if we have reached the end of s1, then we have to insert all the remaining characters of s2
    if i1 == n1:
        return n2 - i2
    if i2 == n2:
        return n1 - i1
    if s1[i1] == s2[i2]:
        return find_min_operations_recurse(s1, s2, i1+1, i2+1)
    # perform deletion
    c1 = 1 + find_min_operations_recurse(s1, s2, i1+1, i2)
    # perform insertion
    c2 = 1 + find_min_operations_recurse(s1, s2, i1, i2+1)
    # perform replacement
    c3 = 1 + find_min_operations_recurse(s1, s2, i1+1, i2+1)
    return min(c1, min(c2, c3))

def main():
  print(find_min_operations("bat", "but"))
  print(find_min_operations("abdca", "cbda"))
  print(find_min_operations("passpot", "ppsspqrt"))


main()
