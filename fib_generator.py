"""
This is a Python program to return back fibonacci numbers
"""



class FibIterator:

    def __init__(self, n):
        super().__init__()
        self.end = n

    def __iter__(self):
        self.x = 0
        self.y = 1
        return self

    def __next__(self):
        if self.y > self.end:
            raise StopIteration
        self.x, self.y = self.y, self.x + self.y
        return self.x


if __name__ == '__main__':
    fib = FibIterator(100)
    for each in fib:
        print(each)
