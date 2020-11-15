class CycleVector:

    def __init__(self, capacity = 4):
        self.end = 0
        self.begin = 0
        self.capacity = capacity
        self.list = [None] * capacity

    def add(self, x):
        if self.end > self.capacity - 1:
            if self.begin > self.capacity // 4:
                self.end = 0
            else:
                self._extend_capacity()
        elif self.end == self.begin - 1:
            self._extend_capacity()
        self.list[self.end] = x
        self.end += 1

    @property
    def size(self):
        return (self.end < self.begin) * self.capacity + self.end - self.begin

    def get(self, i = None):
        if not i:
            return self.list[self.begin]
        if i < 0 or i >= self.capacity:
            return
        else:
            i += self.begin
            if i >= self.capacity:
                i -= self.capacity
        return self.list[i]

    def remove(self):
        if self.size == 0:
            return
        if self.size < self.capacity // 4:
            self._reduce_capacity()
        self.begin += 1
        if self.begin == self.capacity:
            self.begin = 0
            if self.end == self.capacity:
                self.end = 0

    def _extend_capacity(self):
        new_list = [None] * (self.capacity * 2)
        if self.begin > self.end:
            for i, j in enumerate([*range(self.begin, self.capacity), *range(self.end)]):
                new_list[i] = self.list[j]
        else:
            for i, j in enumerate(range(self.begin, self.end)):
                new_list[i] = self.list[j]
        self.capacity *= 2
        self.begin = 0
        self.end = i + 1
        self.list = new_list

    def _reduce_capacity(self):
        new_list = [None] * (self.capacity // 2)
        if self.begin > self.end:
            for i, j in enumerate([*range(self.begin, self.capacity), *range(self.end)]):
                new_list[i] = self.list[j]
        else:
            for i, j in enumerate(range(self.begin, self.end)):
                new_list[i] = self.list[j]
        self.capacity //= 2
        self.begin = 0
        self.end = i + 1
        self.list = new_list


class Queue:

    def __init__(self):
        self.list = CycleVector()

    @property
    def size(self):
        return self.list.size

    def push(self, x):
        self.list.add(x)

    def pop(self):
        val = self.list.get()
        self.list.remove()
        return val

    def first(self):
        return self.list.get()


if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(input().split())
    queue = Queue()
    for el in arr:
        if el[0] == '-':
            print(queue.pop())
            print('del', queue.list.list, queue.list.begin, queue.list.end, queue.size)
        else:
            queue.push(el[1])
            print(f'add {el[1]}', queue.list.list, queue.list.begin, queue.list.end, queue.size)

"""
10
+ 1
-
+ 2
-
+ 3
- 
+ 4
-
+ 5
-

1
10


24
+ 1
+ 2
+ 3
+ 4
-
-
+ 5
+ 6
-
-
+ 7
+ 8
-
-
+ 9
+ 10
+ 11
-
-
-
-
-
+ 12
-

"""