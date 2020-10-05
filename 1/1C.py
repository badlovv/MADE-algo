def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr_s = merge_sort(n, arr)
    print(' '.join(map(str, arr_s)))


def merge_sort(n, arr):
    if n == 1:
        return arr
    arr1 = arr[:n//2]
    arr2 = arr[n//2:]
    arr1 = merge_sort(n//2, arr1)
    arr2 = merge_sort(n - n//2, arr2)
    # print('m_s:', arr1, arr2)
    return merge(arr1, arr2)


def merge(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    i = 0
    j = 0
    arr = []
    while i + j < n1 + n2:
        if i == n1 or (j < n2 and arr2[j] < arr1[i]):
            arr.append(arr2[j])
            j += 1
        else:
            arr.append(arr1[i])
            i += 1
    # print('m:', arr)
    return arr

if __name__ == '__main__':
    main()
