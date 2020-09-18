from collections import deque  # for fast push and pop operations


class Stack:
    """
    Args:
            1) array: is a list or empty


    Functions:

            1) push(element):

            2) pop()

            3) getvalues()
    """

    def __init__(self, array=None, size=None):
        self.__size = None
        if (isinstance(array, list) or isinstance(array, tuple)) and size is not None:
            self.__array = deque(array, maxlen=size)
            self.__size = size
        elif isinstance(array, list) or isinstance(array, tuple):
            self.__array = deque(array)
        elif size is not None:
            self.__array = deque(maxlen=size)
            self.__size = size
        else:
            self.__array = deque()
        # print(self.__array)

    def __len__(self):
        return len(self.__array)

    def __repr__(self):
        return 'Stack([' + ', '.join(map(str, self.__array)) + '])'

    def __iter__(self):
        self.__iter_index = 0
        return self

    def __next__(self):
        if self.__iter_index < len(self):
            result = self.__array[self.__iter_index]
            self.__iter_index += 1
            return result
        else:
            raise StopIteration

    def push(self, element):
        self.__array.append(element)

    def pop(self):
        return self.__array.pop()

    def getvalues(self):
        return list(self.__array)

    def peek(self):
        return self.__array[-1]

    def clear(self):
        self.__array.clear()

    def isfull(self):
        if self.__size is None:
            raise ValueError('Initialize size of Stack')
        return len(self) == self.__size

    def isempty(self):
        if self.__size is None:
            raise ValueError('Initialize size of Stack')
        return len(self) == 0


def main():
    s = Stack(size=5)
    # s = Stack(list(range(10)), size=5)
    # s = Stack(array=[1, 2])
    # s = Stack()
    s.push(3)
    s.push(4)
    s.push(3)
    s.push(4)
    s.push(3)
    s.push(4)
    print(list(s))
    print(s.isfull())
    # s.pop()
    # print(s.isfull())
    print(s.getvalues())
    # print(s.clear())
    print(s)
    print(s.peek())


if __name__ == '__main__':
    main()
