# index: 278816 -> wariant 2
import math

def hashInsert(arr, elem, length):
    i = 0
    count = 0
    surname_hashed = hash(elem.surname)
    h1 = surname_hashed % length
    while True:
        count += 1
        h2 = 1 + (surname_hashed % (length - 2))
        position = (h1 + i * h2) % length
        if arr[position] is None:
            arr[position] = elem
            return count
        i += 1
        if i == length: return count

def create_array(m):
    result = []
    for i in range(m):
        result.append(None)
    return result

class Person:
    def __init__(self, popularity, surname):
        self.popularity = popularity
        self.surname = surname

    def print(self):
        print(self.popularity, self.surname)

length = 17
small_array = create_array(length)
file = open("ASCIInazwiska.txt", encoding="utf8")

for j in range(0, 10):
    line = file.readline().replace("\n", "").split(" ")
    line[0] = int(line[0])
    person = Person(line[0], line[1])
    hashInsert(small_array, person, length)
file.close()

file = open("mala-tablica-test.txt", "w")
for item in small_array:
    if item is None:
        file.write("None\n")
    else:
        file.write(str(item.popularity) + " " + item.surname + "\n")
file.close()

size1, size2, size3, size4, size5, size6 = 16_384, 18_000, 7_351, 10_079, 15_361, 18_041
p1, p2, p3 = 0.35, 0.65, 0.95

sizes = (size1, size2, size3, size4, size5, size6)
percents = p1, p2, p3

for size in sizes:
    for filling in percents:
        arr = create_array(size)
        file = open("ASCIInazwiska.txt", encoding="utf8")
        counter = 0
        testing_size = math.floor(5 * size / 100)

        for n in range(0, math.floor(filling * size)):
            line = file.readline().replace("\n", "").split(" ")
            line[0] = int(line[0])
            person = Person(line[0], line[1])
            hashInsert(arr, person, size)

        for n in range(0, testing_size):
            line = file.readline().replace("\n", "").split(" ")
            line[0] = int(line[0])
            person = Person(line[0], line[1])
            counter += hashInsert(arr, person, size)

        average = counter / testing_size
        file.close()
        print('============================================================================')
        print(f'Rozmiar tablicy: {size}  |  Wypelnienie: {filling}  |  Srednia: {average}')


"""
============================================================================
Rozmiar tablicy: 16384  |  Wypelnienie: 0.35  |  Srednia: 1.6935286935286935
============================================================================
Rozmiar tablicy: 16384  |  Wypelnienie: 0.65  |  Srednia: 4.271062271062271
============================================================================
Rozmiar tablicy: 16384  |  Wypelnienie: 0.95  |  Srednia: 8247.166056166056
============================================================================
Rozmiar tablicy: 18000  |  Wypelnienie: 0.35  |  Srednia: 1.6611111111111112
============================================================================
Rozmiar tablicy: 18000  |  Wypelnienie: 0.65  |  Srednia: 4.193333333333333
============================================================================
Rozmiar tablicy: 18000  |  Wypelnienie: 0.95  |  Srednia: 9045.037777777778
============================================================================
Rozmiar tablicy: 7351  |  Wypelnienie: 0.35  |  Srednia: 1.6539509536784742
============================================================================
Rozmiar tablicy: 7351  |  Wypelnienie: 0.65  |  Srednia: 3.019073569482289
============================================================================
Rozmiar tablicy: 7351  |  Wypelnienie: 0.95  |  Srednia: 125.15258855585832
============================================================================
Rozmiar tablicy: 10079  |  Wypelnienie: 0.35  |  Srednia: 1.687872763419483
============================================================================
Rozmiar tablicy: 10079  |  Wypelnienie: 0.65  |  Srednia: 3.0019880715705765
============================================================================
Rozmiar tablicy: 10079  |  Wypelnienie: 0.95  |  Srednia: 126.23260437375745
============================================================================
Rozmiar tablicy: 15361  |  Wypelnienie: 0.35  |  Srednia: 1.6497395833333333
============================================================================
Rozmiar tablicy: 15361  |  Wypelnienie: 0.65  |  Srednia: 3.1979166666666665
============================================================================
Rozmiar tablicy: 15361  |  Wypelnienie: 0.95  |  Srednia: 126.70833333333333
============================================================================
Rozmiar tablicy: 18041  |  Wypelnienie: 0.35  |  Srednia: 1.5753880266075388
============================================================================
Rozmiar tablicy: 18041  |  Wypelnienie: 0.65  |  Srednia: 3.1596452328159645
============================================================================
Rozmiar tablicy: 18041  |  Wypelnienie: 0.95  |  Srednia: 131.23281596452327
"""
