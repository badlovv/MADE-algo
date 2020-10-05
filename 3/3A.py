import atexit
import io
import sys

_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


def binary_search2(s, e, x):
    if s == (e - 1):
        if s == -1:
            return arr[e]
        elif e == n:
            return arr[s]
        elif x - arr[s] <= arr[e] - x:
            return arr[s]
        else:
            return arr[e]
    m = (s + e) // 2
    if x == arr[m]:
        return arr[m]
    elif x < arr[m]:
        return binary_search(s, m, x)
    else:
        return binary_search(m, e, x)


def binary_search(s, e, x):
    if s == (e - 1):
        if x - arr[s] <= arr[e] - x:
            return arr[s]
        else:
            return arr[e]
    m = (s + e) // 2
    if x == arr[m]:
        return arr[m]
    elif x < arr[m]:
        return binary_search(s, m, x)
    else:
        return binary_search(m, e, x)


if __name__ == '__main__':
    n, _ = map(int, input().split())
    arr = list(map(int, input().split()))
    k_arr = list(map(int, input().split()))
    for x in k_arr:
        print(binary_search(0, n-1, x))


"""
5 5
1 3 5 7 8
2 4 8 1 6

5 5
1 3 3 3 9
2 4 8 1 6

5 5
1 1 1 1 1
2 4 8 1 6

5 5
9 9 9 9 9
2 4 8 1 6

"""