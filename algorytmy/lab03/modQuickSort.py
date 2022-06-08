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


def bubbleSort(arr):
    for j in range(len(arr) - 1):
        for i in range(len(arr) - j - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


def modQuickSort(arr, p, r, c=1):
    if r - p + 1 < c:
        bubbleSort(arr)
    if p < r:
        q = partition(arr, p, r)
        modQuickSort(arr, p, q)
        modQuickSort(arr, q + 1, r)
