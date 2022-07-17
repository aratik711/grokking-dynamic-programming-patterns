"""

Given a set of positive numbers (non zero) and a target sum ‘S’. Each number should be assigned either a ‘+’ or ‘-’ sign. We need to find out total ways to assign symbols to make the sum of numbers equal to target ‘S’.

Example 1:#
Input: {1, 1, 2, 3}, S=1
Output: 3
Explanation: The given set has '3' ways to make a sum of '1': {+1-1-2+3} & {-1+1-2+3} & {+1+1+2-3}
Example 2:#
Input: {1, 2, 7, 1}, S=9
Output: 2
Explanation: The given set has '2' ways to make a sum of '9': {+1+2+7-1} & {-1+2+7+1}
Sum(s1) - Sum(s2) = S
Sum(s1) + Sum(s2) = Sum(num)
=> Sum(s1) - Sum(s2) + Sum(s1) + Sum(s2) = S + Sum(num)
=> 2 * Sum(s1) =  S + Sum(num)
=> Sum(s1) = (S + Sum(num)) / 2
This essentially converts our problem to: “Find count of subsets of the given numbers whose sum is equal to”,
=> (S + Sum(num)) / 2


The above solution has time and space complexity of O(N*S), where ‘N’ represents total numbers and ‘S’ is the desired sum.

"""

def find_target_subsets(num, s):
    if any(i<1 for i in num):
        return -1
    totalSum = sum(num)
    # if 's + totalSum' is odd, we can't find a subset with sum equal to '(s + totalSum) / 2'
    if totalSum < s or (totalSum + s) % 2 == 1:
        return 0
    return count_subsets(num, int((s+totalSum)/2))

def count_subsets(num, sum):
    n = len(num)
    if n == 0:
        return 0
    dp = [ 0 for x in range(sum + 1)]
    dp[0] = 1
    for s in range(1, sum+1):
        dp[s] = 1 if num[0] == s else 0
    for i in range(1, n):
        for s in range(sum, -1, -1):
            if num[i] <= s:
                dp[s] += dp[s-num[i]]
    return dp[sum]

def main():
  print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
  print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()
