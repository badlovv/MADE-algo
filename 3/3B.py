import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


def lower_bound(s, e, x):
    if s == e - 1:
        return e
    m = (s + e) // 2
    if x <= arr[m]:
        return lower_bound(s, m, x)
    else:
        return lower_bound(m, e, x)


if __name__ == '__main__':
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    k = int(input())
    k_arr = [0] * k
    for i in range(k):
        k_arr[i] = list(map(int, input().split()))

    rng = [0] * k
    for i, (x_s, x_e) in enumerate(k_arr):
        s = lower_bound(-1, n, x_s)
        e = lower_bound(-1, n, x_e + 1)
        rng[i] = e-s
    print(' '.join(map(str, rng)))


"""
5
10 1 10 3 4
4
1 10
2 9
3 4
2 2

"""