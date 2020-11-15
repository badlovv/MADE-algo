import sys
from random import randint

UTF8 = "utf-8"


class Node:

    def __init__(self, data: int, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:

    def __init__(self, x=None):
        self.first = Node(x)
        self.last = Node(x)
        self.size = 0

    def insert(self, i, v):
        if i == 0:
            self.prepend(v)
        elif i == self.size:
            self.append(v)
        else:
            new_node = Node(v)
            curr_node = self.get(i)
            curr_node.prev.next = new_node
            new_node.prev = curr_node.prev
            curr_node.prev = new_node
            new_node.next = curr_node
            self.size += 1

    def append(self, x):
        new_node = Node(x)
        if self.size == 0:
            self.first = new_node
            self.last = new_node
        else:
            new_node.prev = self.last
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
            self.first.prev = new_node
            self.first = new_node
        self.size += 1

    def remove_first(self):
        if self.size == 1:
            self.first = self.last = Node(None)
        else:
            self.first = self.first.next
            self.first.prev = None
        self.size -= 1

    def remove(self, i: int):
        if i == 0:
            if self.size == 1:
                self.first = self.last = Node(None)
            else:
                self.first = self.first.next
                self.first.prev = None
        else:
            curr_node = self.first.next
            j = 1
            while j < i:
                curr_node = curr_node.next
                j += 1

            curr_node.prev.next = curr_node.next
            if i == self.size - 1:
                self.last = curr_node.prev
            else:
                curr_node.next.prev = curr_node.prev
        self.size -= 1

    def del_node(self, node):
        if self.size == 1:
            self.first = self.last = Node(None)
        elif node.next == None:
            self.last = node.prev
            node.prev.next = None
        elif node.prev == None:
            self.first = node.next
            node.next.prev = None
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
        self.size -= 1

    def get(self, i):
        if self.size == 0 or i >= self.size:
            return
        curr_node = self.first
        j = 0
        while j < i:
            curr_node = curr_node.next
            j += 1
        return curr_node


class Map:
    def __init__(self, size):
        self.rng = 1000
        self.M = 5 * size + randint(1, self.rng)
        self.P = 7 * size + randint(1, self.rng)
        self.A = randint(50, 100)
        self.ord_a = ord('a')
        self.list = [LinkedList() for i in range(self.M)]
        self.link = LinkedList()
        self.cnt = 0

    def put(self, k, v):
        i = self._h(k)
        size = self.list[i].size
        curr_node = self.list[i].first
        j = 0
        while j < size and curr_node.data is not None:
            if curr_node.data[0] == k:
                curr_node.data[1] = v
                return
            curr_node = curr_node.next
            j += 1

        self.link.append(None)
        self.cnt += 1
        self.list[i].append([k, v, self.link.last])
        self.link.last.data = self.list[i].last

    def delete(self, k):
        i = self._h(k)
        curr_node = self.list[i].first
        size = self.list[i].size
        # print(i, curr_node, curr_node.data)
        j = 0
        while j < size and curr_node.data is not None:
            if curr_node.data[0] == k:
                self.link.del_node(curr_node.data[2])
                self.list[i].remove(j)
                # print(curr_node.data, self.link.last.data, self.link.first.data, self.list[i].last.data)
                break
            curr_node = curr_node.next
            j += 1

    def get(self, k, node_mode=False):
        i = self._h(k)
        size = self.list[i].size
        curr_node = self.list[i].first
        j = 0
        while j < size and curr_node.data is not None:
            if curr_node.data[0] == k:
                if node_mode:
                    return curr_node
                return curr_node.data[1]
            curr_node = curr_node.next
            j += 1
        if node_mode:
            return
        else:
            return 'none'

    def prev(self, k):
        curr_node = self.get(k, True)
        if curr_node:
            curr_link_node = curr_node.data[2]
            if curr_link_node.prev:
                return curr_link_node.prev.data.data[1]
        return 'none'

    def next(self, k):
        curr_node = self.get(k, True)
        if curr_node:
            curr_link_node = curr_node.data[2]
            if curr_link_node.next:
                return curr_link_node.next.data.data[1]
        return 'none'

    def _h(self, word):
        res = 0
        for l in word:
            l = ord(l) - self.ord_a + 1
            res = (res * self.A + l) % self.P
        return res % self.M


if __name__ == '__main__':
    SIZE = 10 ** 5
    buff = sys.stdin.buffer.read().splitlines()
    arr = [None] * len(buff)
    for i in range(len(buff)):
        arr[i] = buff[i].decode(UTF8).split()
    s = Map(SIZE)
    r = []
    for op in arr:
        if op[0] == 'put':
            s.put(op[1], op[2])
        elif op[0] == 'get':
            # print(s.get(op[1]))
            r.append(s.get(op[1]))
        elif op[0] == 'prev':
            r.append(s.prev(op[1]))
        elif op[0] == 'next':
            r.append(s.next(op[1]))
        else:
            s.delete(op[1])
    buff_out = ('\n'.join(r)).encode(UTF8)
    sys.stdout.buffer.write(buff_out)


"""
put zero a
delete zero
put zero b
get zero
prev zero
next zero
put one b
put two c
put three d
put four e
get two
delete two
put two a
prev two
next asddas
delete one
delete three
get two
prev two
next two
next four
prev four
"""

