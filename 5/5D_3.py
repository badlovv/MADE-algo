import sys
from random import randint

UTF8 = "utf-8"

class Set:
    def __init__(self, size):
        self.rng = 1000
        self.M = 5 * size + randint(1, self.rng)
        self.P = 7 * size + randint(1, self.rng)
        self.A = randint(1, self.rng)
        self.list = [None] * self.M

    def add(self, k):
        i = self._h(k)
        while self.list[i] is not None:
            if self.list[i] == k:
                return
            i = (i + 1) % self.M
        self.list[i] = k

    def remove(self, k):
        i = self._h(k)
        while self.list[i] is not None:
            if self.list[i] == k:
                self.list[i] = None
                break
            i = (i + 1) % self.M

    def exists(self, k):
        i = self._h(k)
        while self.list[i] is not None:
            if self.list[i] == k:
                return True
            i = (i + 1) % self.M
        return False

    def _h(self, k):
        return (self.A * k % self.P) % self.M


class MultiMap:
    def __init__(self, size):
        self.rng = 1000
        self.M = 15 * size + randint(1, self.rng)
        self.P = 21 * size + randint(1, self.rng)
        self.A = randint(50, 100)
        self.ord_a = ord('a')
        self.list = [None] * self.M

    def put(self, k, v):
        i = self._h(k)
        while self.list[i] is not None:
            if self.list[i] == [k, v]:
                return
            i = (i + 1) % self.M
        self.list[i] = [k, v]

    def remove(self, k, v=None):
        i = self._h(k)
        while self.list[i] is not None:
            if self.list[i] == [k, v]:
                self.list[i] = None
                break

            i = (i + 1) % self.M

    def delete(self, k, v=None):
        i = self._h(k)
        del_ind = []
        for j, el in enumerate(self.list[i]):
            if el[0] == k:
                if el[1] == v:
                    self.list[i].pop(j)
                    break
                elif v is None:
                    del_ind.append(j)
        for j in reversed(del_ind):
            self.list[i].pop(j)

    def get(self, k):
        i = self._h(k)
        vals = []
        for j, el in enumerate(self.list[i]):
            if el[0] == k:
                vals.append(el[1])
        return len(vals), vals

    def _h(self, word):
        res = 0
        for l in word:
            l = ord(l) - self.ord_a + 1
            # res = (res * self.A + l)
            res = (res * self.A + l) % self.P
        # print(res % self.M)
        return res % self.M


if __name__ == '__main__':
    SIZE = 10 ** 5
    buff = sys.stdin.buffer.read().splitlines()
    arr = [None] * len(buff)
    for i in range(len(buff)):
        arr[i] = buff[i].decode(UTF8).split()
    s = MultiMap(SIZE)
    r = []
    for op in arr:
        if op[0] == 'put':
            s.put(op[1], op[2])
        elif op[0] == 'get':
            l, values = s.get(op[1])
            r.append(f'{l} {" ".join(map(str, values))}')
        elif op[0] == 'delete':
            s.delete(op[1], op[2])
        else:
            s.delete(op[1])
    buff_out = ('\n'.join(r)).encode(UTF8)
    sys.stdout.buffer.write(buff_out)
    #
    # test = LinkedList()
    # test.append('1')
    # test.append('2')
    # # test.remove(1)
    # test.remove(0)
    # test.append('3')
    # test.append('4')
    #
    #
    # test.remove(0)
    # test.insert(1, '5')
    # test.insert(2, '6')
    # print(test.first.data, test.get(0).data, test.get(1).data, test.get(2).data)

"""
put hello privet
put bye poka
get hello
get bye
delete hello
get hello

privet
poka
none


put 1 1
put 2 2
put 2 3
get 1
get 2
delete 1
get 1
put 1 4
get 1
delete bye
delete kek
get hello
get lol
get 2
put 3 5
get 3
"""

