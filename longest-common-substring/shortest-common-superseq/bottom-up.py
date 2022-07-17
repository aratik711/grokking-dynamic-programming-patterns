"""

Given two sequences ‘s1’ and ‘s2’, write a method to find the length of the shortest sequence which has ‘s1’ and ‘s2’ as subsequences.

Example 2:

Input: s1: "abcf" s2:"bdcf"
Output: 5
Explanation: The shortest common super-sequence (SCS) is "abdcf".
Example 2:

Input: s1: "dynamic" s2:"programming"
Output: 15
Explanation: The SCS is "dynprogrammicng".

If the character s1[i] matches s2[j], the length of the SCS would be the one plus the length of the SCS till i-1 and j-1 indexes in the two strings.
If the character s1[i] does not match s2[j], we will consider two SCS: one without s1[i] and one without s2[j]. Our required SCS length will be the shortest of these two super-sequences plus one.

The time and space complexity of the above algorithm is O(n*m)

"""

def find_SCS_length(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[0 for x in range(n2+1)]for y in range(n1+1)]

    # if one of the strings is of zero length, SCS would be equal to the length of the other string
    for i in range(n1+1):
        dp[i][0] = i
    for j in range(n2+1):
        dp[0][j] = j

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
    return dp[n1][n2]

def main():
  print(find_SCS_length("abcf", "bdcf"))
  print(find_SCS_length("dynamic", "programming"))


main()
