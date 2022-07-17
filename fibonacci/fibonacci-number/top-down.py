"""


Fibonacci numbers are a series of numbers in which each number is the sum of the two preceding numbers. First few Fibonacci numbers are: 0, 1, 1, 2, 3, 5, 8, …

Mathematically we can define the Fibonacci numbers as:

    Fib(n) = Fib(n-1) + Fib(n-2), for n > 1

    Given that: Fib(0) = 0, and Fib(1) = 1

"""
def calculateFibonacci(num):
    mem = [-1 for i in range(num+1)]
    return calculateFibonacci_recurse(mem, num)

def calculateFibonacci_recurse(mem, num):
    if num < 2:
        return num
    if mem[num] >= 0:
        return mem[num]
    mem[num] = calculateFibonacci_recurse(mem, num-1) + calculateFibonacci_recurse(mem, num-2)
    return mem[num]


def main():
  print("5th Fibonacci is ---> " + str(calculateFibonacci(5)))
  print("6th Fibonacci is ---> " + str(calculateFibonacci(6)))
  print("7th Fibonacci is ---> " + str(calculateFibonacci(7)))


main()
