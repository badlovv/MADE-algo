import atexit
import io
import sys

# _INPUT_LINES = sys.stdin.read().splitlines()
# input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    for k in range(n):
        l = k
        while l > 0 and arr[l-1] > arr[l]:
            temp = arr[l-1]
            arr[l-1] = arr[l]
            arr[l] = temp
            l -= 1
    print(' '.join(map(str, arr)))


if __name__ == '__main__':
    main()