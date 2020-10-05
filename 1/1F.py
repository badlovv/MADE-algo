def royal_sort(kings):
    for i, king in enumerate(kings):
        kings[i] = list([king[0], str(numerate(king[1]))]) + king
    for king in sorted(kings):
        print(' '.join(king[2:]))


def numerate(r_numb):
    d_nums = [rome_numbers[k] for k in list(r_numb)]
    for i in range(len(d_nums[:-1])):
        if d_nums[i] < d_nums[i+1]:
            d_nums[i] = - d_nums[i]
    return sum(d_nums)


if __name__ == '__main__':
    n = int(input())
    kings = []
    rome_numbers = {'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for _ in range(n):
        kings.append(list(input().split()))
    royal_sort(kings)
