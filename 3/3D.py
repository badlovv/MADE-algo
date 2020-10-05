def func(x):
    y = 0
    for el in n_arr:
        y += el // x
    return y


def b_search(val, s, e, f):
    m = 1
    while e - s > 1:
        m = (s + e) // 2
        if f(m) >= val:
            s = m
        else:
            e = m
    if f(m) < val:
        return m - 1
    else:
        return m


if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    n_arr = [0] * n
    for i in range(n):
        n_arr[i] = int(input())
    end = sum(n_arr) // k + 1
    print(b_search(k, 0, end, func))

"""
4 11
802
743
457
539

200

4 11
810
743
457
539

2 5
1
1

2 5
3
3

4 3
1
1
1
1

4 1
15
15
15
15

2 12
600
600



"""
