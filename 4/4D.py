import sys


class Heap:

    def __init__(self):
        self.list = []
        self.size = 0
        self.list_cnt = 0
        self.cnt = 0
        self.pos = []

    def insert(self, x):
        i = self.size
        self.list.append([x, self.cnt])

        self.pos.append(self.list_cnt)
        self.list_cnt += 1
        self.cnt += 1

        self.size += 1
        self._sift_up(i)

    def pop_min(self):
        self.pos.append(None)
        self.cnt += 1

        if self.size == 0:
            return '*'

        self._swap(0, self.size - 1)
        self.list_cnt -= 1
        self.size -= 1

        i = 0
        self._sift_down(i)

        m, pos = self.list.pop()
        self.pos[pos] = None
        return m, pos + 1

    def decrease_value(self, k, val):
        self.pos.append(None)
        self.cnt += 1

        if self.pos[k - 1] is None:
            return

        pos = self.pos[k - 1]
        self.list[pos] = [val, k - 1]
        self._sift_up(pos)

    def _swap(self, i, j):
        self.list[i], self.list[j] = self.list[j], self.list[i]

        p_i = self.list[i][1]
        p_j = self.list[j][1]
        self.pos[p_i], self.pos[p_j] = self.pos[p_j], self.pos[p_i]

    def _sift_up(self, i):
        while i > 0 and self.list[i] < self.list[(i - 1) // 2]:
            self._swap(i, (i - 1) // 2)
            i = (i - 1) // 2

    def _sift_down(self, i):
        while 2 * i + 1 < self.size:
            curr = self.list[i]
            left = self.list[2 * i + 1]
            if 2 * i + 2 == self.size:
                right = [float('inf')]
            else:
                right = self.list[2 * i + 2]
            if left < curr and left < right:
                self._swap(i, 2 * i + 1)
                i = 2 * i + 1
            elif right < curr:
                self._swap(i, 2 * i + 2)
                i = 2 * i + 2
            else:
                break


if __name__ == '__main__':
    arr = sys.stdin.readlines()
    arr = [el.split() for el in arr]
    heap = Heap()
    for el in arr:
        if el[0] == 'push':
            heap.insert(int(el[1]))
        elif el[0] == 'decrease-key':
            heap.decrease_value(int(el[1]), int(el[2]))
        else:
            print(' '.join(map(str, heap.pop_min())))


"""
push 3
push 4
push 2
extract-min
decrease-key 3 1
push 8
push 2
decrease-key 6 1
extract-min
extract-min
extract-min

2 3
1 6
2 7
3 1


extract-min
push 10
decrease-key 2 8
push 4
extract-min
"""