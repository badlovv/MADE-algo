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


if __name__ == '__main__':
    SIZE = 10 ** 6
    buff = sys.stdin.buffer.read().splitlines()
    arr = [None] * len(buff)
    for i in range(len(buff)):
        arr[i] = buff[i].decode(UTF8).split()
    s = Set(SIZE)
    r = []
    for op in arr:
        if op[0] == 'insert':
            s.add(int(op[1]))
        elif op[0] == 'exists':
            r.append(str(s.exists(int(op[1]))).lower())
        else:
            s.remove(int(op[1]))

    buff_out = ('\n'.join(r)).encode(UTF8)
    sys.stdout.buffer.write(buff_out)

"""
insert 2
insert 5
insert 3
exists 2
exists 4
insert 2
delete 2
exists 2

true
false
false

"""

