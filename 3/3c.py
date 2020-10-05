from math import log10


def func(x):
    return x ** 2 + x ** 0.5


def b_search(val, s, e, eps, f):
    max_i = int(((log10(e / eps) // 3) + 1) * 10)
    for i in range(1, max_i):
        m = (s + e) / 2
        if f(m) < val:
            s = m
        else:
            e = m
    return round(e, 6)


if __name__ == '__main__':
    EPS = 10 ** (-6)
    MAX_SIZE = 10 ** 5
    MIN_SIZE = 0
    value = float(input().strip())
    print(b_search(value, MIN_SIZE, MAX_SIZE, EPS, func))

