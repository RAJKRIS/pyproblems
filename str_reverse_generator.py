"""
Python program to reverse a string using iterator
"""


class StringRevIterator:

    def __init__(self, string):
        super().__init__()
        self.string = string
        self.length = len(string)


    def __iter__(self):
        return self

    def __next__(self):
        self.length -= 1
        if self.length < 0:
            raise StopIteration
        return self.string[self.length]


def StringRevGenerator(string):
    i = len(string) - 1
    while i >= 0:
        yield string[i]
        i -= 1
    raise StopIteration


def main():
    s = StringRevIterator('John')
    print ("Using Iterator")
    for each in s:
        print (each)
    print ("Using Generator")
    for each in StringRevGenerator('John'):
        print (each)


if __name__ == '__main__':
    main()
