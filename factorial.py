"""
Program to find factorial of a number
"""


def factorial_rec(n):
    if n > 1:
        return n * factorial_rec(n-1)
    return 1

def factorial(n):
    fact = 1
    while n > 1:
        fact = fact * n
        n -= 1
    return fact

def main():
    print ("Factorial using recursion")
    print ("Factorial of 5: ", factorial_rec(5))
    print ("Factorial without recursion")
    print ("Factorial of 6: ", factorial(6))

if __name__ == '__main__':
    main()
