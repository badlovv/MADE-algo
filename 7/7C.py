import sys

UTF8 = 'utf-8'


class Fenwick:

    def __init__(self, arr, n):
        self.t = self.t(arr, n)
        self.arr = arr
        self.n = n

    def add(self, i, x):
        j = i
        while j < self.n:
            self.t[j] += x
            j = j | (j + 1)

    def get(self, i):
        s = 0
        while i >= 0:
            s += self.t[i]
            i = self.f(i) - 1
        return s

    def set(self, i, x):
        d = x - self.arr[i]
        self.arr[i] = x
        self.add(i, d)

    def t(self, arr, n):
        t = [0] * n
        for i in range(n):
            j = self.f(i)
            while j <= i:
                t[i] += arr[j]
                j += 1
        return t

    def rsq(self, s, e):
        if s == 0:
            return self.get(e)
        return self.get(e) - self.get(s - 1)

    @staticmethod
    def f(i):
        return i & (i+1)


if __name__ == '__main__':
    buffer = sys.stdin.buffer.read().splitlines()
    buf = [None] * len(buffer)
    for i in range(len(buffer)):
        buf[i] = buffer[i].decode(UTF8).split()
    n = int(buf[0][0])
    arr = list(map(int, buf[1]))
    q_arr = buf[2:]

    fw = Fenwick(arr, n)
    ans = []
    for q in q_arr:
        if q[0] == 'sum':
            ans.append(fw.rsq(int(q[1]) - 1, int(q[2]) - 1))
        else:
            fw.set(int(q[1]) - 1, int(q[2]))

    print_buffer = ('\n'.join(map(str, ans))).encode(UTF8)
    sys.stdout.buffer.write(print_buffer)

"""
5
1 2 3 4 5
sum 2 5
sum 1 5
sum 1 4
sum 2 4
set 1 10
set 2 3
set 5 2
sum 2 5
sum 1 5
sum 1 4
sum 2 4



"""

