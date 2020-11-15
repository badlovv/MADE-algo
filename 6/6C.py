def solve(arr, n):
    dp = [1] * n
    prevs = [None] * n
    end = 0

    for i in range(1, n):
        prev = None
        curr_max = 0
        j = i - 1
        while j >= 0:
            if curr_max < dp[j] and arr[j] < arr[i]:
                curr_max = dp[j]
                prev = j
            elif curr_max > j:
                break
            j -= 1
        dp[i] += curr_max
        prevs[i] = prev
        if dp[end] <= curr_max:
            end = i
    # print(dp)
    length = dp[end]

    sequence = []
    while end is not None:
        sequence.append(arr[end])
        end = prevs[end]
    sequence.reverse()

    return length, sequence

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    length, sequence = solve(arr, n)
    print(length)
    print(' '.join(map(str, sequence)))

"""
8
1 4 1 5 3 3 4 2


"""

