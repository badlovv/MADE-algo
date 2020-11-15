# import atexit
# import io
# import sys
#
# _INPUT = sys.stdin.read().splitlines()
# input = iter(_INPUT).__next__
# _OUTPUT = io.StringIO()
# sys.stdout = _OUTPUT
#
#
# @atexit.register
# def write():
#     sys.__stdout__.write(_OUTPUT.getvalue())


class Node:

    def __init__(self, data: int, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self, x=None):
        self.first = Node(x)
        self.last = Node(x)
        self.size = 0

    def append(self, x):
        new_node = Node(x)
        if self.size == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.size += 1

    def prepend(self, x):
        new_node = Node(x)
        if self.size == 0:
            self.first = new_node
            self.last = new_node
        else:
            new_node.next = self.first
            self.first = new_node
        self.size += 1

    def remove_first(self):
        if self.size == 1:
            self.first = self.last = Node(None)
        else:
            self.first = self.first.next
        self.size -= 1

    def remove(self, i: int):
        if i == 0:
            if self.size == 1:
                self.first = self.last = Node(None)
            else:
                self.first = self.first.next
        else:
            prev_node = self.first
            curr_node = self.first.next
            j = 1
            while j < i:
                prev_node = curr_node
                curr_node = prev_node.next
                j += 1
            prev_node.next = curr_node.next
            if i == self.size - 1:
                self.last = prev_node
        self.size -= 1


class Stack:

    def __init__(self, x=None):
        self.list = LinkedList(x)
        self.min_list = LinkedList()

    @property
    def size(self):
        return self.list.size

    def push(self, x):
        self.list.prepend(x)
        if self.min_list.first.data is None or self.min_list.first.data >= self.list.first.data:
            self.min_list.prepend(x)

    def remove(self):
        if self.min_list.first.data == self.list.first.data:
            self.min_list.remove(0)
        self.list.remove(0)

    def last(self):
        return self.list.last.data

    def min(self, ):
        return self.min_list.first.data


if __name__ == '__main__':
    n = int(input())
    arr = [None] * n
    for i in range(n):
        arr[i] = list(map(int, input().split()))
    stack = Stack()
    min_list = []
    for op in arr:
        # print(op[0], stac.list.first.data, stac.list.last.data, stac.list.size)
        if op[0] == 1:
            stack.push(op[1])
        elif op[0] == 2:
            stack.remove()
        else:
            min_list.append(stack.min())
    print('\n'.join(map(str, min_list)))

"""
8
1 2
1 3
1 -3
3
2
3
2
3

6
1 2
2
1 0
2
1 3
3

4
1 2
2
1 0
2
"""

