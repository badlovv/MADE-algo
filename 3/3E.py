def func(s):
    if s < min_s:
        return 0
    return 1 + int((1 / x) * (s - min_s)) + int((1 / y) * (s - min_s))


def lower_bound(s, e, f, val):
    # print(s, e, val)
    if s >= e - 1:
        return e
    m = (s + e) // 2
    if val <= f(m):
        return lower_bound(s, m, f, val)
    else:
        return lower_bound(m, e, f, val)

#
# def b_search(s, e, f):
#     # max_i = int(((log10(e / eps) // 3) + 1) * 10)
#     for i in range(1, 10):
#         m1 = s + (e - s) / 3
#         m2 = s + 2 * (e - s) / 3
#         # print(s,e,f(s), f(e), m1, m2, f(m1), f(m2))
#         if f(m1) < f(m2):
#             e = m2
#         else:
#             s = m1
#     return e


if __name__ == '__main__':
    n, x, y = list(map(int, input().split()))
    min_s = min(x, y)
    end = min_s * n
    print(lower_bound(min_s, end, func, n))
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
