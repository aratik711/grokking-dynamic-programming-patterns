"""


Fibonacci numbers are a series of numbers in which each number is the sum of the two preceding numbers. First few Fibonacci numbers are: 0, 1, 1, 2, 3, 5, 8, …

Mathematically we can define the Fibonacci numbers as:

    Fib(n) = Fib(n-1) + Fib(n-2), for n > 1

    Given that: Fib(0) = 0, and Fib(1) = 1

The time complexity of the above algorithm is exponential O(2^n) as we are making two recursive calls in the same function. The space complexity is O(n) which is used to store the recursion stack.



"""
def calculateFibonacci(num):
    if num < 2:
        return num
    return calculateFibonacci(num-1) + calculateFibonacci(num-2)


def main():
  print("5th Fibonacci is ---> " + str(calculateFibonacci(5)))
  print("6th Fibonacci is ---> " + str(calculateFibonacci(6)))
  print("7th Fibonacci is ---> " + str(calculateFibonacci(7)))


main()
