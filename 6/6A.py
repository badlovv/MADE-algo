def solve(n, k, a):
    d = [0] * n
    a = [0] + a + [0]
    p = [None] * n

    for i in range(1, n):
        max_i = i - 1
        j = max(0, i - k)
        while j < i:
            if d[j] > d[max_i]:
                max_i = j
            j += 1
        d[i] = d[max_i] + a[i]
        p[i] = max_i

    steps = []
    i = n - 1
    steps.append(str(i + 1))
    while i > 0:
        steps.append(str(p[i] + 1))
        i = p[i]
    steps.reverse()

    return d[n-1], steps


if __name__ == '__main__':
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    M, steps = solve(N, K, arr)
    print(M)
    print(len(steps) - 1)
    print(' '.join(map(str, steps)))

"""
d[1]=0; a[1]=0; a[n]=0;
for (int i=2;i<=n;++i){
int num_max = i - 1;
//поиск предыдущего столбика с максимальным количеством монет
for(int j=max(1,i-k);j<=i-1;++j)
if (d[j]>d[num_max]) {
num_max=j;
}
d[i]=d[num_max]+a[i]; //Текущее максимальное значение
p[i] = num_max;
}
printf("%d\n", d[n]);
"""


"""
5 3
2 -3 5

5 2
2 -3 5

2 2

15 2
-1 -1 2 3 0 0 -1 0 -1 -1 -1 -1 -1

7 5
-1 -1 -1 -1 -1

5 1
2 -3 5

2 2
2 -3 5

12 2
2 -1 -1 -1 2 3 1 2 0 0

5 4
-1 -2 -5
"""

