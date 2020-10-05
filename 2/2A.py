from random import choice

def main():
    pass


def find(k, s, e):
    if e - s == 1:
        return arr[k]
    x = choice(arr[s:e+1])
    m1, m2 = split(s, e, x)

    if k < m1 + 1:
        return find(k, s, m1+1)
    else:
        return find(k, m2, e)


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


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    p = int(input())
    q_arr = []
    for i in range(p):
        q_arr.append(list(map(int, input().split())))
        print(find(q_arr[i][2], q_arr[i][0], q_arr[i][1]))

