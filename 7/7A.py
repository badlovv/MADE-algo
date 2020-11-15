C_A = 2 ** 16
C_B = 2 ** 30


def gen_a(x, y, a_0):
    arr = [0] * n
    arr[0] = a_0
    for i in range(1, n):
        arr[i] = (x * arr[i - 1] + y) % C_A
    return arr


def gen_c(z, t, b_0):
    arr = [0] * (2 * m)
    arr[0] = b_0 % n
    prev_b = b_0
    for i in range(1, 2 * m):
        prev_b = ((z * prev_b + t) % C_B)
        arr[i] = prev_b % n
    return arr

#
# def gen_c(b):
#     return [b[i] % n for i in range(len(b))]


def cumsum(arr):
    cumsum = [0] * (n + 1)
    cumsum[0] = 0
    for i in range(1, n + 1):
        cumsum[i] = cumsum[i - 1] + arr[i - 1]
    return cumsum


if __name__ == '__main__':
    n, x, y, a_0 = list(map(int, input().split()))
    m, z , t, b_0 = list(map(int, input().split()))
    arr_a = gen_a(x, y, a_0)
    arr_c = gen_c(z, t, b_0)
    print(arr_a, arr_c)
    # arr_c = gen_c(arr_b)
    cumsum_a = cumsum(arr_a)
    del arr_a
    sum = 0
    for i in range(m):
        sum += cumsum_a[max(arr_c[2 * i], arr_c[2 * i + 1]) + 1] - cumsum_a[min(arr_c[2 * i], arr_c[2 * i + 1])]
        # print(sum)

    print(sum)



"""
3 1 2 3
3 1 -1 4


"""

