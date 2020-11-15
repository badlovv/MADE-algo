class Vector:

    def __init__(self, capacity = 4):
        self.size = 0
        self.capacity = capacity
        self.list = [None] * capacity

    def get(self, i = None):
        if not i:
            return self.list[self.size - 1]
        if i >= self.size or i < 0:
            return
        return self.list[i]

    def add(self, x):
        if self.size > self.capacity - 1:
            self._extend_capacity()
        self.list[self.size] = x
        self.size += 1

    def remove(self):
        if self.size == 0:
            return
        if self.size < self.capacity // 4:
            self._reduce_capacity()
        self.size -= 1

    def _extend_capacity(self):
        self.capacity *= 2
        new_list = [None] * self.capacity
        for i in range(self.size):
            new_list[i] = self.list[i]
        self.list = new_list

    def _reduce_capacity(self):
        self.capacity //= 2
        new_list = [None] * self.capacity
        for i in range(self.size):
            new_list[i] = self.list[i]
        self.list = new_list


class Stack:

    def __init__(self):
        self.list = Vector()

    @property
    def size(self):
        return self.list.size

    def push(self, x):
        self.list.add(x)

    def pop(self):
        val = self.list.get()
        self.list.remove()
        return val

    def last(self):
        return self.list.get()


def evaluate(stack):
    op = stack.pop()
    if op == '+' or op == '-' or op == '*':
        a = str(evaluate(stack))
        b = str(evaluate(stack))
        return eval(b + op + a)
    else:
        return op


if __name__ == '__main__':
    arr = input().split()
    stack = Stack()
    for el in arr:
        stack.push(el)
    print(evaluate(stack))

"""
8 9 + 1 7 - *

-102

"""