def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r + 1):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    if i < r:
        return i
    else:
        return i - 1


def quickSort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quickSort(arr, p, q)
        quickSort(arr, q + 1, r)
