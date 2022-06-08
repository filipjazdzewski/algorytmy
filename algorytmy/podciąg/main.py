def fill(arr, line1, line2):
    for j in range(0, len(line2) + 1):
        arr.append([])
        for i in range(0, len(line1) + 1):
            if j == 0 or i == 0:
                arr[j].append(0)
            elif line1[i-1] == line2[j-1]:
                arr[j].append(arr[j-1][i-1] + 1)
            else:
                arr[j].append(max(arr[j][i-1], arr[j-1][i]))

def printArr(arr, line1, line2):
    for j in range(0, len(arr) + 1):
        for i in range(0, len(arr[j-1]) + 1):
            if i == 0 and j > 1:
                print(line2[j-2], end=" ")
            elif j == 0 and i > 1:
                print(line1[i-2], end=" ")
            elif (j == 0 or i == 0) and j != i:
                print("\u03BB", end=" ")
            elif j == 0 and i == 0:
                print("-", end=" ")
            else:
                print(f'{arr[j-1][i-1]}', end=" ")
        print()

def dfs(arr):
    seen = set() # seen set
    stack = []
    result = [[]]
    h = len(arr) # height
    w = len(arr[0]) # width
    stack.append((h-1, w-1))

    while len(stack) > 0:
        p = stack.pop() # current position
        seen.add(p)

        if p[0] > 0 and p[1] > 0:
            cent = arr[p[0]][p[1]]  # current value
            left = arr[p[0]][p[1] - 1]  # value to the left
            top = arr[p[0] - 1][p[1]]  # value above
            diag = arr[p[0] - 1][p[1] - 1]  # value diagonal

            if (p[0]-1, p[1]-1) not in seen and left == top == diag and diag + 1 == cent:
                stack.append((p[0]-1, p[1]-1))
                result[-1].append((p[0], p[1]))
            else:
                if (p[0], p[1]-1) not in seen and left >= top:
                    stack.append((p[0], p[1]-1))
                if (p[0]-1, p[1]) not in seen and top >= left:
                    stack.append((p[0]-1, p[1]))
        elif result[-1] != []:
            result.append([])

    return result

f = open("input.txt", "r")
one = f.readline().strip()
two = f.readline().strip()
f.close()

array = []
fill(array, one, two)
printArr(array, one, two)
result = list(map(lambda l: list(map(lambda t: one[t[1]-1], reversed(l))), filter(lambda l: len(l) > 0, dfs(array))))
print()
print(result)