def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr_s, c = merge_sort(n, arr)
    print(c)


def merge_sort(n, arr):
    if n == 1:
        return arr, 0
    arr1 = arr[:n//2]
    arr2 = arr[n//2:]
    arr1, c1 = merge_sort(n//2, arr1)
    arr2, c2 = merge_sort(n - n//2, arr2)
    return merge(arr1, arr2, c1 + c2)


def merge(arr1, arr2, c):
    n1 = len(arr1)
    n2 = len(arr2)
    counter = c
    i = 0
    j = 0
    arr = []
    while i + j < n1 + n2:
        if i == n1:
            arr.append(arr2[j])
            j += 1
        elif j < n2 and arr2[j] < arr1[i]:
            arr.append(arr2[j])
            j += 1
            counter += n1 - i
        else:
            arr.append(arr1[i])
            i += 1
    return arr, counter


if __name__ == '__main__':
    main()
