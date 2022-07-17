"""

Given a set of positive numbers, partition the set into two subsets with a minimum difference between their subset sums.

Example 1:#
Input: {1, 2, 3, 9}
Output: 3
Explanation: We can partition the given set into two subsets where the minimum absolute difference
between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.
Example 2:#
Input: {1, 2, 7, 1, 5}
Output: 0
Explanation: We can partition the given set into two subsets where the minimum absolute difference
between the sum of numbers is '0'. Following are the two subsets: {1, 2, 5} & {7, 1}.
Example 3:#
Input: {1, 3, 100, 4}
Output: 92
Explanation: We can partition the given set into two subsets where the minimum absolute difference
between the sum of numbers is '92'. Here are the two subsets: {1, 3, 4} & {100}.

The above solution has time and space complexity of O(N*S), where ‘N’ represents total numbers and ‘S’ is the total sum of all the numbers.



"""

def can_partition(num):
    s = sum(num)
    n = len(num)
    dp = [ [False for x in range(int(s/2)+1)] for y in range(n)]
    for i in range(n):
        dp[i][0] = True

    for j in range(1, int(s/2)+1):
        dp[0][j] = num[0] == j

    # process all subsets for all sums
    for i in range(1,n):
        for j in range(1, int(s/2)+1):
            # if we can get the sum 's' without the number at index 'i'
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= num[i]:
                dp[i][j] = dp[i-1][j-num[i]]
    sum1 = 0
    for i in range(int(s/2), -1, -1):
        if dp[n-1][i]:
            sum1 = i
            break
    sum2 = s - sum1
    return abs(sum2 - sum1)

def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 9])))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
  print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()
