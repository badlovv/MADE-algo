
def solve(n, m, arr):
    def pos(i, j):
        if i < 0 or j < 0 or i >= n or j >= m:
            return float('-inf')
        else:
            return arr[i][j]

    for i in range(n):
        for j in range(m):
            if i == j == 0:
                continue
            else:
                arr[i][j] += max(pos(i - 1, j), pos(i, j - 1))
    steps = []
    j = m - 1
    i = n - 1
    while j > 0 or i > 0:
        if pos(i - 1, j) < pos(i, j - 1):
            steps.append("R")
            j -= 1
        else:
            steps.append("D")
            i -= 1
    steps.reverse()
    steps_str = ''.join(steps)

    return arr[n - 1][m - 1], steps_str


if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    money, path = solve(N, M, arr)
    print(money)
    print(path)

"""
3 3
0 2 -3
2 -5 7
1 2 0

"""

