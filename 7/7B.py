from math import log2

C_1 = 23
C_2 = 21563
C_3 = 16714589
U_1 = 17
U_2 = 751
U_3 = 2
V_1 = 13
V_2 = 593
V_3 = 5


def gen_array():
    arr = [0] * n
    arr[0] = a_1
    for i in range(1, n):
        arr[i] = (C_1 * arr[i-1] + C_2) % C_3
    return arr


def next_query(i, u_i, v_i, r_i):
    u = ((U_1 * u_i + U_2 + r_i + U_3 * i) % n) + 1
    v = ((V_1 * v_i + V_2 + r_i + V_3 * i) % n) + 1
    return u, v


def min_sparse_matrix():
    sparse = [[None] * (LOG2[n - i] + 1) for i in range(n)]
    for l in range(n):
        sparse[l][0] = arr[l]
    for k in range(1, len(sparse[0])):
        for l in range(n - POWER2S[k] + 1):
            sparse[l][k] = min(sparse[l][k - 1], sparse[l + POWER2S[k - 1]][k - 1])
    return sparse


def solve():
    u_next, v_next = u_1, v_1
    for i in range(1, m + 1):
        u, v = u_next, v_next
        if v >= u:
            k = LOG2[v - u]
            r = min(min_arr[u - 1][k], min_arr[v - POWER2S[k]][k])
        else:
            k = LOG2[u - v]
            r = min(min_arr[v - 1][k], min_arr[u - POWER2S[k]][k])
        u_next, v_next = next_query(i, u, v, r)
    return u, v, r


def count_log2s():
    log2s = [0] * (n + 1)
    for i in range(1, n + 1):
        log2s[i] = int(log2(i))
    return log2s


def count_power2s(log2s):
    return [2 ** i for i in range(log2s[-1] + 1)]


if __name__ == '__main__':
    n, m, a_1 = list(map(int, input().split()))
    u_1, v_1 = list(map(int, input().split()))
    LOG2 = count_log2s()
    POWER2S = count_power2s(LOG2)

    arr = gen_array()
    min_arr = min_sparse_matrix()
    u_n, v_n, r_n = solve()
    print(u_n, v_n, r_n)



"""
10 8 12345
3 9

"""

