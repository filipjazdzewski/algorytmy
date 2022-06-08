from timeit import default_timer as timer
from random import randint
from quickSort import quickSort
from modQuickSort import modQuickSort
import sys

typeOfData = ["DANE LOSOWE", "DANE NIEKORZYSTNE"]
sys.setrecursionlimit(10000)
print()

for i in range(len(typeOfData)):
    data = []
    if i == 0:
        arr100 = list(range(100))
        arr500 = list(range(500))
        arr1000 = list(range(1000))
        arr2500 = list(range(2500))

        arr100.reverse()
        arr500.reverse()
        arr1000.reverse()
        arr2500.reverse()

        data = [arr100, arr500, arr1000, arr2500]

    else:
        arr100 = [randint(0, 100) for _ in range(100)]
        arr500 = [randint(0, 500) for _ in range(500)]
        arr1000 = [randint(0, 1000) for _ in range(1000)]
        arr2500 = [randint(0, 2500) for _ in range(2500)]

        data = [arr100, arr500, arr1000, arr2500]

    print(typeOfData[i])
    print(f"rozmiar tablicy N | {' ' * 6} quickSort {' ' * 7} | {' ' * 3} modifiedQuickSort {' ' * 3} |")
    for arr in data:
        length = len(arr)
        temp = arr

        start1 = timer()
        quickSort(arr, round(length/2), length - 1)
        stop1 = timer()

        start2 = timer()
        modQuickSort(temp, round(length/2), length - 1)
        stop2 = timer()

        print(f"{' ' * (10 - len(str(length)))} {length} {' ' * 5} | {stop1 - start1}s {' ' * (22 - len(str(stop1 - start1)))} | {stop2 - start2}s {' ' * (23 - len(str(stop2 - start2)))} |")
    print()
