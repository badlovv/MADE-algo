

def split(s, e, x):
    m = s
    d = 0
    for i in range(s, e):
        if arr[i] < x:
            arr[m - d: i + 1] = [arr[i]] + arr[m - d: m + 1],
            m += 1
        elif arr[i] == x:
            arr[i], arr[m + d] = arr[m + d], arr[i]
            d += 1
        print(f'i:{i}, m:{m}, d:{d}, arr:{arr}')
    return m, m - d


def quicksort(s, e):
    if e - s <= 1:
        return
    # if e - s == 2 and arr[s] == arr[s+1]:
    #     return
    # step = max((e-s)//3, 1)
    # x = sum(arr[s:e][::-step]) / min(3, e-s)
    x = arr[(s + e)//2]
    m1, m2 = split(s, e, x)
    print(f'[{s}, {e}], {x}, [{m1}, {m2}]', arr)

    quicksort(s, m1 + 1)
    quicksort(m2, e)

from random import choice

def quick_sort(s, e):
    if e - s < 1:
        return

    x = choice(arr[s:e+1])
    i = s
    j = e
    while i <= j:
        while arr[i] < x:
            i += 1
        while arr[j] > x:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    quick_sort(s, j)
    quick_sort(i, e)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    # quick_sort(0, n)
    quick_sort(0, n-1)
    print(' '.join(map(str, arr)))

