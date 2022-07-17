"""


Fibonacci numbers are a series of numbers in which each number is the sum of the two preceding numbers. First few Fibonacci numbers are: 0, 1, 1, 2, 3, 5, 8, …

Mathematically we can define the Fibonacci numbers as:

    Fib(n) = Fib(n-1) + Fib(n-2), for n > 1

    Given that: Fib(0) = 0, and Fib(1) = 1

The above solution has a time complexity of O(n) but a constant space complexity O(1)


"""
def calculateFibonacci(num):
    if num < 2:
        return num
    n1, n2, temp = 0, 1, 0
    for i in range(2, num+1):
        temp = n1 + n2
        n1 = n2
        n2 = temp
    return n2


def main():
  print("5th Fibonacci is ---> " + str(calculateFibonacci(5)))
  print("6th Fibonacci is ---> " + str(calculateFibonacci(6)))
  print("7th Fibonacci is ---> " + str(calculateFibonacci(7)))


main()
