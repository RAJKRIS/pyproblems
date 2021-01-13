"""
Find out if a number is armstrong
"""
from functools import reduce

def armstrong_with_reduce(n):
    ord = len(str(n))
    s = reduce(lambda x, y: int(x)**ord + int(y)**ord,  str(n))
    return s == n

def armstrong(n):
    ord, s = len(str(n)), 0
    for each in str(n):
        s += int(each) ** ord
    return s == n

def main():
    print("Armstrong Number")
    print("Is 153 Armstrong:", "Yes" if armstrong(153) else "No")


if __name__ == '__main__':
    main()
