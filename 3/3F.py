from math import log10, sqrt


def func(x):
    return sqrt(a ** 2 + (1 - x) ** 2) / vf + sqrt(x ** 2 + (1 - a) ** 2) / vp


def b_search(s, e, eps, f):
    max_i = int(((log10(e / eps) // 3) + 1) * 10)
    print(max_i)
    for i in range(1, max_i):
        m1 = s + (e - s) / 3
        m2 = s + 2 * (e - s) / 3
        # print(s,e,f(s), f(e), m1, m2, f(m1), f(m2))
        if f(m1) < f(m2):
            e = m2
        else:
            s = m1
    return e


if __name__ == '__main__':
    EPS = 10 ** (-6)
    END = 1
    START = 0
    vp, vf = list(map(int, input().split()))
    a = float(input())
    print(b_search(START, END, EPS, func))

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
